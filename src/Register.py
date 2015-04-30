import glob, os
import cv2 as cv
from direc import alphFolder
from Crop import Start_Crop, clean
from database import *
import re
import subprocess
from subprocess import check_call

class Register(object):
    def __init__(self, firstname, lastname, passphrase, group, room):#initialise class with data from gui
        self.firstname = firstname.lower()
        self.lastname = lastname.lower()
        self.passphrase = passphrase.lower()
        self.group   = group
        self.room = room
        self.name = str(lastname)+"_"+str(firstname) # lastname_forename format for folder names
        self.name = self.name.lower()
        self.userpath = ""
        alphFolder()

    def submit(self, imgnum):#Upload all pictures to the lapis space

        subprocess.call('rsync %s/face%d_crop.jpg c1312433@lapis.cs.cf.ac.uk:/home/c1312433/CM2301/%s/%s' % (self.userpath, imgnum, self.userpath[3:8], self.userpath[9:]), shell=True)
        #os.system('rsync %s/face%d_crop.jpg c1312433@lapis.cs.cf.ac.uk:/home/c1312433/CM2301/%s/%s' % (self.userpath, imgnum, self.userpath[3:8], self.userpath[9:]))THIS IS DEPRECATED


    def CreateFolder(self):#Create the necessary folder for the user in the file structure
        path = "../usr/"+self.passphrase[:1]+"/"+self.name
        print path

        if not os.path.exists(path):
            os.makedirs(path)
            with open(path+"/speech.txt", "w+") as theirfile: # Then save a personal record of their passphrase in their folder
                    theirfile.write(str(self.passphrase))


        print "Initiating remote sync"
        subprocess.call('rsync --recursive ../usr/ c1312433@lapis.cs.cf.ac.uk:/home/c1312433/CM2301/usr/', shell=True)
        #os.system('rsync --recursive %s c1312433@lapis.cs.cf.ac.uk:/home/c1312433/CM2301/%s/' % (self.userpath, self.userpath[3:8]))
        print "Done."

        print "User folder created!\nStarting face registration - Please keep still!"
        
        for x in range(4,-1,-1):
            time.sleep(1)
            print "Capturing in.." + str(x+1)        

        print "Capturing now - Please keep still, whilst facing the camera!"

    def folderCheck(self):#check if folder is duplicated, if yes increment number at end to allow people with same name and passphrase

        f = open('../passphrases.txt', 'a+')
        
        print "Pulling relevant files from remote server"
        subprocess.call('rsync -chavzP --stats c1312433@lapis.cs.cf.ac.uk:/home/c1312433/CM2301/usr/%s ../usr/' % (self.passphrase[:1]), shell=True)            
        # os.system("rsync -chavzP --stats c1312433@lapis.cs.cf.ac.uk:/home/c1312433/CM2301/usr/%s ../usr/" % (self.passphrase[:1]))
        print "Done."

        foldercheck = 1
        while(True):
            if os.path.exists("../usr/"+self.passphrase[:1]+"/"+ self.name):   
                notfound = 1
                if notfound:
                    if self.name[-1].isdigit() == True:
                        slicenum = len(str(int(re.search(r'\d+', self.name).group())))
                        self.name = self.name[:-slicenum]
                        self.name+=str(foldercheck)

                    else:
                        self.name+=str(foldercheck)

                    print "The name " + self.name[:-1] + " was taken, reassigned: " + self.name
                    foldercheck+=1


            else:
                print "Found name: " + str(self.name)
                self.userpath = "../usr/"+self.passphrase[:1]+"/"+self.name
                f.write(str(self.passphrase)+"\n") # MOVE TO ELSE NOW
                subprocess.call('rsync ../passphrases.txt c1312433@lapis.cs.cf.ac.uk:/home/c1312433/CM2301/', shell=True) # sync with remote
                print "Creating user folder.."
                self.CreateFolder()
                break   
        
    def capImg(self):#code to capture image, detect if face is looking at camera
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

            path = '../usr/'+str(self.userpath)+"/"
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
            Start_Crop(self.userpath, x)
            self.submit(x)

            

        subprocess.call('rsync %s/speech.txt c1312433@lapis.cs.cf.ac.uk:/home/c1312433/CM2301/%s/%s' % (self.userpath, self.userpath[3:8], self.userpath[9:]), shell=True)
        #os.system('rsync %s/speech.txt c1312433@lapis.cs.cf.ac.uk:/home/c1312433/CM2301/%s/%s' % (self.userpath, self.userpath[3:8], self.userpath[9:]))

        print "Sync complete.\n"

        self.databaseSync()
        clean(self.userpath)
        print "User's path is: " + self.userpath
        print "FINISHED\n"
        #Start_Crop(userpath)


    def databaseSync(self):
        db = database()
        groupid = db.get_group_id_from_name(self.group)
        db.add_user(self.userpath, self.passphrase, self.firstname, self.lastname, groupid, self.room)
        db.exit()

    #ImageFromCam(path)
if __name__ == '__main__':
    try:
        register = Register("firstname", "lastname", "passphrase", "group", "room")
        register.folderCheck()
        register.capImg()
    except (Exception) as err:
        print err
