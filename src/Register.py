'''
This file will open the webcam up, then extract the image, this image then will be cropped
so that it only shows the face of the person, which can then later be compared.

Phase I - Capture image
'''
__author__ = "shazaibahmad"

import sys
import mmap
import glob, os 
import cv2 as cv
from dir import alphFolder
from Crop import Start_Crop
import database

passphrase = ''

def UserInput(): # Take user input
	firstname = raw_input("Enter forename: ")
	lastname = raw_input("Enter lastname: ")
	passphrase = raw_input("Enter passphrase: ")
	passphrase = passphrase.lower()

	name = str(lastname)+"_"+str(firstname) # lastname_forename format for folder names

	
	alphFolder()
	while(True):
		with open("../passphrases.txt", "a+") as myfile:
			if passphrase in myfile.read():
				print "Already exists."
				passphrase = raw_input("Enter passphrase: ") # If so, they must re-enter
				passphrase = passphrase.lower()

			else: 				
				myfile.write(str(passphrase)+"\n")
				CreateFolder(name, passphrase)
				break


def CreateFolder(name, passphrase):
	path = "../usr/"+passphrase[:1]+"/"+name
	print path

	if not os.path.exists(path):
		os.makedirs(path)
		with open(path+"/speech.txt", "w+") as theirfile: # Then save a personal record of their passphrase in their folder
				theirfile.write(str(passphrase))

	ImageFromCam(path)

def ImageFromCam(userpath):
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
			try:
				cv.imwrite(path+fname+str(capNumb)+ext, frame)
				print "Capped"
				Start_Crop(userpath, capNumb)
<<<<<<< HEAD
				os.system('rsync %s c1312433@lapis.cs.cf.ac.uk:/home/c1312433/CM2301/%s/' % (userpath[:8], userpath[3:8]))
                                print userpath[:8]
                                print userpath[3:8]
#                                db = database.database()
 #                               db.add_user(passphrase,                             
=======
				#os.system('rsync %s c1312433@lapis.cs.cf.ac.uk:/home/c1312433/CM2301/%s/' % (userpath[:8], userpath[3:8]))
>>>>>>> 331b109ad5820e4224a5a2fde873a97ff549f584

			except Exception:
				print Exception
					
					#print "Captured"
			capNumb+=1	

			if capNumb == 6:
				break # from while loop
					

			# if : 
			# 	print "Facial features were not found!"

		elif key == 113:
			cap.release()
			cv.destroyAllWindows()
			print "Exiting.."
			sys.exit(0)

	print "Captured " + str(capNumb-1) + " images!" 
	cap.release()
	cv.destroyAllWindows()
	#Start_Crop(userpath)

UserInput()

