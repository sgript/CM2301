'''
This file will open the webcam up, then extract the image, this image then will be cropped
so that it only shows the face of the person, which can then later be compared.

Phase I - Capture image
'''
__author__ = "shazaibahmad"

import time
import sys
import cv2 as cv
import glob, os 
from Crop import Start_Crop

def ImageFromCam():
	cap = cv.VideoCapture(0)
	cap.set(1, 20.0)
	cap.set(3,640)  
	cap.set(4,480) 

               
	Face_Cascade = cv.CascadeClassifier('../cv/haarcascade_frontalface_default.xml')
	Eye_Cascade = cv.CascadeClassifier('../cv/haarcascade_eye.xml') # Later may add eyes.


	while True:
		# Capture frame-by-frame
		ret, frame = cap.read()
		Gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

		Faces = Face_Cascade.detectMultiScale(Gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30), flags = cv.cv.CV_HAAR_SCALE_IMAGE)
		#print Faces
		eyes = None
			# Draw a rectangle around the faces
		for (x, y, w, h) in Faces: # To draw rectangle for face
			cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


			roi_gray = Gray[y:y+h, x:x+w]
			roi_color = frame[y:y+h, x:x+w]
			eyes = Eye_Cascade.detectMultiScale(roi_gray)

			# for (ex,ey,ew,eh) in eyes:
			# 	cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)


		cv.imshow('Webcam - Active (Press Q to finish, C to capture)', frame)

		
		found = 0
		if not isinstance(Faces, tuple) and not isinstance(eyes, tuple):	
			found = 1
		else:
			found = 0

		print found

		path = '../img/'
		fname = 'face'
		ext = '.jpg'
		capNumb = 0
		key = cv.waitKey(99) 
		if key > 127:
			key = key & 255 # Deal with silly keyboard inputs 
		if key == 99:

			if found == 1:
				for x in range(0, 5):
					try:
						cv.imwrite(path+fname+str(capNumb)+ext, frame)

					except Exception:
						print Exception
					
					print "Captured"
					capNumb+=1	

				if x == 4:
					break # from while loop

			else: 
				print "Facial features were not found!"

		elif key == 113:
			cap.release()
			cv.destroyAllWindows()
			print "Exiting.."
			sys.exit(0)

	cap.release()
	cv.destroyAllWindows()

ImageFromCam()
Start_Crop("../img")
#execfile('Crop.py')
