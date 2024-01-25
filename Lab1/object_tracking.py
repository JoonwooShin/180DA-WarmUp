"""
My code was written based on the given references for Bounding box contours and filtering based on color, as well as converting to different color schemes. The tutorial for video cameras was also used to obtain a stream of frames.
https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html
https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html

No additional features were added
"""
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # HSV
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # RED
    mask1 = cv2.inRange(frame_HSV, (0, 70, 50), (10, 255, 255))
    mask2 = cv2.inRange(frame_HSV, (170, 70, 50), (180, 255, 255))
    thresh1 = mask1 | mask2

    # Part 3: H:88 S:183 V:128
    thresh2 = cv2.inRange(frame_HSV, (80, 50, 50), (100, 255, 255))

    # thresh 1 = frame_HSV, thresh2 = Color picker
    contours,hierarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(frame_HSV,(x,y),(x+w,y+h),(255,0,0),3)

    # RGB
    frame_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # RED
    thresh3 = cv2.inRange(frame_RGB, (128, 0, 0), (255, 50, 50))

    contours2,hierarchy2 = cv2.findContours(thresh3, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours2:
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    
    

    # Display the resulting frame
    cv2.imshow('frame_RGB', frame)
    cv2.imshow('frame_HSV', frame_HSV)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()