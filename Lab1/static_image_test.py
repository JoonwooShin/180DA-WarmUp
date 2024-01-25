import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Load the image
img = cv.imread('static_image.png')
assert img is not None, "file could not be read, check with os.path.exists()"

# convert to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Edge Detection
edges = cv.Canny(gray, 100, 200)

# Adaptive Gaussian Thresholding
# img_blur = cv.medianBlur(img,5)
thresh = cv.adaptiveThreshold(edges,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
thresh_color = cv.cvtColor(thresh, cv.COLOR_GRAY2BGR)

# Find the contours
contours,hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

# For each contour, find the bounding rectangle and draw it
for cnt in contours:
    area = cv.contourArea(cnt)
    if area > 20000:
        x,y,w,h = cv.boundingRect(cnt)
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv.imshow('img', img) 
cv.waitKey(0) 

cv.destroyAllWindows()