import cv2

cap = cv2.VideoCapture(0)
cap.set(1, 20.0)
cap.set(3,640)  
cap.set(4,480) 

fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
video_writer = cv2.VideoWriter('videoout.avi',fourcc, 20.0, (640,480))


faceCascade = cv2.CascadeClassifier('/usr/local/Cellar/opencv/2.4.9/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('/usr/local/Cellar/opencv/2.4.9/share/OpenCV/haarcascades/haarcascade_eye.xml')


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    
    X = 0
    Y = 0
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        X = x
        Y = y

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eyeCascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,255),2)

    # Display the resulting frame
    cv2.imshow('Webcam - Active (Press Q to finish)', frame)
    video_writer.write(frame)

    if cv2.waitKey(1) & X+Y > 400:
    #if cv2.waitKey(1) & 0xFF == ord('q'):
        print X,Y
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()