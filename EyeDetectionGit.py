import numpy as np
import cv2


faceCascade = cv2.CascadeClassifier('C:/00. PERSONAL/Jai/Udemy DataScience/Opencv/opencv/sources/data/haarcascades/haarcascade_righteye_2splits.xml')

cap = cv2.VideoCapture(0)

while(cap.isOpened()):  # check !
    # capture frame-by-frame
    ret, frame = cap.read()

    if ret: # check ! (some webcam's need a "warmup")
        # our operation on frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
        )
        font = cv2.FONT_HERSHEY_SIMPLEX
        for (x, y, w, h) in faces:                               
            cv2.putText(frame,'AFP',(x,y+40),font,0.8 ,(0,255,0),2,cv2.LINE_4)
            cv2.imshow('Video',frame)
        
        key = cv2.waitKey(1)

        if key in [ord('a'), 1048673]:
            print('a pressed!')
        elif key in [27, 1048603]: # ESC key to abort, close window
            cap.release()    
            cv2.destroyAllWindows()
            break
