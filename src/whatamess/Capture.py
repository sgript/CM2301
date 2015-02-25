'''
This file will open the webcam up, then extract the image, this image then will be cropped
so that it only shows the face of the person, which can then later be compared.

Phase I - Capture image
'''

__author__ = "shazaibahmad"

import cv2 as cv

def ImageFromCam():
	cap = cv.VideoCapture(0)
	cap.set(1, 20.0)
	cap.set(3,640)  
	cap.set(4,480) 

	 
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
	    cv.imshow('Webcam - Active (Press Q to finish)', frame)
	    
	    key = cv.waitKey(99)
	    if key & 255== 99:
	    	cv.imwrite('../img/face.jpg', frame)
	    	break
	    # if cv.waitKey(1) & 0xFF == ord('c'):
	    #     cv.imwrite('../img/face.jpg', frame)
	    #     print "captured"


	# When everything is done, release the capture
	cap.release()
	cv.destroyAllWindows()

ImageFromCam()
execfile('Crop.py')
