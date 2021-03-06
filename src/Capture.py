'''
This file will open the webcam up, then extract the image, this image then will be cropped
so that it only shows the face of the person, which can then later be compared to REGISTERED images.

Phase II - Capture image
'''

import time, sys
import cv2 as cv
from Crop import Start_Crop, clean
import os

class Capture:
	def ImageFromCam(self):
		cap = cv.VideoCapture(0) # Initial sets for opencv window
		cap.set(1, 20.0)
		cap.set(3,640)  
		cap.set(4,480) 

		 
		Face_Cascade = cv.CascadeClassifier('../cv/haarcascade_frontalface_default.xml') # Classifiers used for face/eyes det
		Eye_Cascade = cv.CascadeClassifier('../cv/haarcascade_eye.xml') 

		eyes = None # Later uses to detect if facing forward
		found = 0
		while True:
		    # Capture frame-by-frame
		    ret, frame = cap.read()

		    Gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

		    Faces = Face_Cascade.detectMultiScale(Gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30), flags = cv.cv.CV_HAAR_SCALE_IMAGE)
		    
		    # Draw a rectangle around the faces
		    for (x, y, w, h) in Faces: # To draw rectangle for face
		        #cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) # Unused for now
		        # For now no rectangles around the face, already checking for faults in real-time

		        roi_gray = Gray[y:y+h, x:x+w]
		        #roi_color = frame[y:y+h, x:x+w] # Unused for now
		        eyes = Eye_Cascade.detectMultiScale(roi_gray)

		        #for (ex,ey,ew,eh) in eyes:
		        #cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

		    # Display the resulting frame
		    cv.imshow('Webcam - Active (Press Q to finish) - Auto capture', frame)


		    msg = ""
		    if not isinstance(Faces, tuple) and not isinstance(eyes, tuple): # If eyes/face values are being found
		    	found = 1
		    	msg = "Facial features found!" # Say they're being found
		    else:
		    	found = 0
		    	msg = "Facial features NOT found!" # Else say they're not being found

		    print msg
		    
		    time.sleep(.4)
		    key = cv.waitKey(20)

		    if key: # Ensure 
		    	if found == 1:
		    		cv.imwrite('../capturedimg/face1.jpg', frame)
		    		Start_Crop('../capturedimg', 1)
		    		
		    		break

		    	else:
		    		print "Facial features were not found!"


		    if key == 113:
				cap.release()
				cv.destroyAllWindows()
				print "Exiting.."
				sys.exit(0)
		

		cap.release()
		cv.destroyAllWindows()
		clean('../capturedimg')

