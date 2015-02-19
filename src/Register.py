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

def ImageFromCam():
	cap = cv.VideoCapture(0)
	cap.set(1, 20.0)
	cap.set(3,640)  
	cap.set(4,480) 

        picturesNo = 1
               
	Face_Cascade = cv.CascadeClassifier('../cv/haarcascade_frontalface_default.xml')
	#Eye_Cascade = cv.CascadeClassifier('./cv/haarcascade_eye.xml') # Later may add eyes.
	while True:
		# Capture frame-by-frame
		ret, frame = cap.read()
		Gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

		Faces = Face_Cascade.detectMultiScale(Gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30), flags = cv.cv.CV_HAAR_SCALE_IMAGE)

			# Draw a rectangle around the faces
		for (x, y, w, h) in Faces: # To draw rectangle for face
			cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

			# Display the resulting frame
		cv.imshow('Webcam - Active (Press Q to finish, C to capture)', frame)
		
		path = '../img/'
		fname = 'face'
		ext = '.jpg'
		#picturesnameNo = 1
		key = cv.waitKey(99) #Wait for key input, with a delay of 99ms
		if key > 127:
			key = key & 255 # Deal with silly keyboard inputs 
		if key == 99:
                        print picturesNo
			while picturesNo <= 5:
			# JACK ---> ADD SOME SLEEP OR INSTEAD OF WHILE LOOP, COUNT KEY PRESSES TO 5 THEN BREAK
				time.sleep(.4)
				try:
					cv.imwrite(path+fname+str(picturesNo)+ext, frame)
				except Exception:
					print Exception			
				print "captured"
                                picturesNo = picturesNo + 1
                                print picturesNo 
				break
                        if picturesNo == 6:
                               break
		elif key == 113:
                        cap.release()
                        cv.destroyAllWindows()
                        print "Bye bye!"
			sys.exit(0)

	# When everything is done, release the capture
	cap.release()
	cv.destroyAllWindows()

ImageFromCam()
execfile('Crop.py')
