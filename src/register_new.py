import sys
import mmap
import glob, os
import cv2 as cv
from direc import alphFolder
from Crop import Start_Crop
from database import *

class Register(object):
    def __init__(self, firstname, lastname, passphrase, group, room):
        self.firstname = firstname.lower()
        self.lastname = lastname.lower()
        self.passphrase = passphrase.lower()
        self.group   = group
        self.room = room
        self.name = str(lastname)+"_"+str(firstname) # lastname_forename format for folder names
        self.name = self.name.lower()
        self.userpath = "../usr/"+self.passphrase[:1]+"/"+self.name
        alphFolder()

    def submit(self, groups, userpath, rooms, imgnum):
        os.system('rsync %s/face%d_crop.jpg c1312433@lapis.cs.cf.ac.uk:/home/c1312433/CM2301/%s/%s' % (self.userpath, imgnum, self.userpath[3:8], self.userpath[9:]))
        db = database.database()
        db.add_user(self, self.userpath, self.passphrase, self.firstname, self.lastname, groups, rooms)


    def CreateFolder(self, name, passphrase):
        path = "../usr/"+passphrase[:1]+"/"+name
        print path

        if not os.path.exists(path):
            os.makedirs(path)
            with open(path+"/speech.txt", "w+") as theirfile: # Then save a personal record of their passphrase in their folder
                    theirfile.write(str(passphrase))


        print "Initiating remote sync"
        os.system('rsync --recursive %s c1312433@lapis.cs.cf.ac.uk:/home/c1312433/CM2301/%s/' % (self.userpath, self.userpath[3:8]))
        print "Done."

    def folderCheck(self, name, passphrase):

        foldercheck = 0
        while(True):
            if os.path.exists("../usr/"+passphrase[:1]+"/"+name):   
                notfound = 1
                if notfound:
                    if name[-1].isdigit() == True:
                        slicenum = len(str(int(re.search(r'\d+', name).group())))
                        name = name[:-slicenum]
                        name+=str(foldercheck)

                    else:
                        name+=str(foldercheck)

                    print "The name " + name[:-1] + " was taken, re-assigned: " + name
                    foldercheck+=1


            else:
                print "Found name: " + str(name)
                f.write(str(passphrase)+"\n") # MOVE TO ELSE NOW
                print "Creating user folder.."
                CreateFolder(name, passphrase)
                break   
        
    def capImg(self, userpath):
        cap = cv.VideoCapture(0)
        cap.set(1, 20.0)
        cap.set(3,640)  
        cap.set(4,480) 

                   
        Face_Cascade = cv.CascadeClassifier('../cv/haarcascade_frontalface_default.xml')
        Eye_Cascade = cv.CascadeClassifier('../cv/haarcascade_eye.xml') # Later may add eyes.

        capNumb = 0
        eyes = None
        found = 0
        while True:

            # Capture frame-by-frame
            ret, frame = cap.read()
            Gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            Faces = Face_Cascade.detectMultiScale(Gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30), flags = cv.cv.CV_HAAR_SCALE_IMAGE)
            #print Faces
                # Draw a rectangle around the faces
            for (x, y, w, h) in Faces: # To draw rectangle for face

                roi_gray = Gray[y:y+h, x:x+w]
                eyes = Eye_Cascade.detectMultiScale(roi_gray)

            cv.imshow('Webcam - Active (Press Q to finish, C to capture)', frame)

            
            msg = ""
            if not isinstance(Faces, tuple) and not isinstance(eyes, tuple):    
                found = 1
                msg = "Facial features found!"
            else:
                found = 0
                msg = "Facial features NOT found!"

            print msg

            path = '../usr/'+str(userpath)+"/"
            fname = 'face'
            ext = '.jpg'
            
            key = cv.waitKey(5)
            if key > 127:
                key = key & 255 # Deal with silly keyboard inputs 
            if key:
                if found:
                    try:
                        # time.sleep(1)
                        cv.imwrite(path+fname+str(capNumb)+ext, frame)
                        print "Captured"

                    except Exception:
                        print Exception
                            
                    capNumb+=1  
                    print "Please wait.."

                    if capNumb == 6:
                        break # from while loop
                else:
                    print "Facial features were not found!"     

            if key == 113:
                cap.release()
                cv.destroyAllWindows()
                print "Exiting.."
                sys.exit(0)

        cap.release()
        cv.destroyAllWindows()
        print "All captured, you may rest now."
        print "Syncing local directory to remote - This may take a while"
        for x in range(0,6):
            Start_Crop(userpath, x)
            submit(self.groups, self.userpath, self.rooms, x)
        os.system('rsync %s/speech.txt c1312433@lapis.cs.cf.ac.uk:/home/c1312433/CM2301/%s/%s' % (userpath, userpath[3:8], userpath[9:]))
        print "Sync complete.\n"

        clean(userpath)
        print "User's path is: " + userpath
        print "FINISHED\n"
        #Start_Crop(userpath)


    #ImageFromCam(path)
if __name__ == '__main__':
    try:
        register = Register("firstname", "lastname", "passphrase", "group", "room")
        register.folderCheck("name", "passphrase")
        register.capImg("userpath")
    except (Exception) as err:
        print err
