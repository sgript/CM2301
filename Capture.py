#import numpy as np
import cv2


cap = cv2.VideoCapture(0)
cap.set(1, 20.0)
cap.set(3,640)  
cap.set(4,480) 

fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
video_writer = cv2.VideoWriter('videoout.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    
    ret, frame = cap.read()
    if ret==True:

        cv2.imshow('Webcam - Active (Press Q to finish)',frame)
        
        video_writer.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
video_writer.release()
cv2.destroyAllWindows()