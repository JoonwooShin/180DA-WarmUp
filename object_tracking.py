import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # HSV
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask1 = cv2.inRange(frame_HSV, (0, 70, 50), (10, 255, 255))
    mask2 = cv2.inRange(frame_HSV, (170, 70, 50), (180, 255, 255))
    thresh1 = mask1 | mask2

    contours,hierarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(frame_HSV,(x,y),(x+w,y+h),(255,0,0),3)

    # RGB

    mask3 = cv2.inRange(frame, (0, 70, 50), (10, 255, 255))
    mask4 = cv2.inRange(frame, (170, 70, 50), (180, 255, 255))
    thresh2 = mask1 | mask2

    contours2,hierarchy2 = cv2.findContours(thresh2, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours2:
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    
    

    # Display the resulting frame
    cv2.imshow('frame', frame)
    cv2.imshow('frame_HSV', frame_HSV)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()