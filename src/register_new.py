import sys
import mmap
import glob, os
import cv2 as cv
from dir import alphFolder
from Crop import Start_Crop

class register(object):
    def __init__(self, firstname, lastname, passphrase, group, room):
		self.firstname = firstname.lower()
		self.lastname = lastname.lower()
		self.passphrase = passphrase.lower()
		self.group	 = group
		self.room = room
		self.name = str(lastname)+"_"+str(firstname) # lastname_forename format for folder names
		self.name = self.name.lower()
		self.userpath = "../usr/"+self.passphrase[:1]+"/"+name

    def submit(self, groups, rooms):
		os.system('rsync --recursive %s c1312433@lapis.cs.cf.ac.uk:/home/c1312433/CM2301/%s/' % (userpath, userpath[3:8]))
		os.system('rsync %s/face%d_crop.jpg c1312433@lapis.cs.cf.ac.uk:/home/c1312433/CM2301/%s/%s' % (self.userpath, capNumb, self.userpath[3:8], self.userpath[9:]))
		db = database.database()
		db.add_user(self, self.userpath, self.passphrase, self.firstname, self.lastname, groups, rooms)

    def checkPassphraseValidity(self):
        if self.passphrase.isDigit():
            return False
    	els:
			while(True):
		        with open("../passphrases.txt", "a+") as myfile:
		            if passphrase in myfile.read():
		                return False

	def capImg(self):
        cap = cv.VideoCapture(0)
		cap.set(1, 20.0)
		cap.set(3,640)
		cap.set(4,480)

		Face_Cascade = cv.CascadeClassifier('../cv/haarcascade_frontalface_default.xml')
		Eye_Cascade = cv.CascadeClassifier('../cv/haarcascade_eye.xml') # Later may add eyes.

		capNumb = 0

		while True:
			# Capture frame-by-frame
			ret, frame = cap.read()
			Gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

			Faces = Face_Cascade.detectMultiScale(Gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30), flags = cv.cv.CV_HAAR_SCALE_IMAGE)
			#print Faces
			eyes = None
				# Draw a rectangle around the faces
			for (x, y, w, h) in Faces: # To draw rectangle for face
				#cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
				# For now no rectangles around the face, already checking for faults in real-time

				roi_gray = Gray[y:y+h, x:x+w]
				roi_color = frame[y:y+h, x:x+w]
				eyes = Eye_Cascade.detectMultiScale(roi_gray)

				# Don't need to draw rectangle around the eyes
				# for (ex,ey,ew,eh) in eyes:
				# 	cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)


			cv.imshow('Webcam - Active (Press Q to finish, C to capture)', frame)


			found = 0
			if not isinstance(Faces, tuple) and not isinstance(eyes, tuple):
				found = 1
			else:
				found = 0

			print found

			path = '../usr/'+str(userpath)+"/"
			fname = 'face'
			ext = '.jpg'

			key = cv.waitKey(5)
			if key > 127:
				key = key & 255 # Deal with silly keyboard inputs
			if key:
				if found:
					try:
						cv.imwrite(path+fname+str(capNumb)+ext, frame)
						print "Captured"
						Start_Crop(userpath, capNumb)

						print "userpath is " + userpath
						print "userpath[3:8] is " + userpath[3:8]

					except Exception:
						print Exception

					capNumb+=1

					if capNumb == 6:
						break # from while loop
				else:
					print "Facial features were not found!"

			if key == 113:
				cap.release()
				cv.destroyAllWindows()
				print "Exiting.."
				sys.exit(0)


		os.system('rsync %s/speech.txt c1312433@lapis.cs.cf.ac.uk:/home/c1312433/CM2301/%s/%s' % (userpath, userpath[3:8], userpath[9:]))
		print "userpath = " + userpath
		print "userpath[:8] = " + userpath[:8]
		print "userpath[3:8] = " + userpath[3:8]
		print "Captured " + str(capNumb-1) + " images!"
		cap.release()
		cv.destroyAllWindows()

  	def CreateFolder(self):
	path = "../usr/"+passphrase[:1]+"/"+name
	print path

	if not os.path.exists(path):
		os.makedirs(path)
		with open(path+"/speech.txt", "w+") as theirfile: # Then save a personal record of their passphrase in their folder
				theirfile.write(str(passphrase))

	ImageFromCam(path)
