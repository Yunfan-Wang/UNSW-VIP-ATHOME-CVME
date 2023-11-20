# Testing canny edge detection 

import cv2 as cv
import numpy as np
import matplotlib as plt

# Define canny thresholds (max)
thresLowMax = 200
thresHighMax = 500

# Define image to use
imgpath = './hallwayfloor.jpeg'
imgpath2 = './hallway2.jpeg'

img = cv.imread(imgpath)
img2 = cv.imread(imgpath2)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

# Declare default trackbar values
thresLow = 100
thresHi = 200

# Trackbar callback functions for thresholds
def trackbar_low_callback(val):
    thresLow = val
    gray_blur = cv.bilateralFilter(gray, 15, 40, 40)
    gray_blur2 = cv.bilateralFilter(gray2, 15, 40, 40)
    
    edges = cv.Canny(gray_blur, thresLow, thresHi)
    edges2 = cv.Canny(gray_blur2, thresLow, thresHi)
    
    cv.imshow("Canny edge 2", edges2)
    cv.imshow("Canny edge", edges)

def trackbar_high_callback(val):
    thresHi = val
    gray_blur = cv.bilateralFilter(gray, 15, 40, 40)
    gray_blur2 = cv.bilateralFilter(gray2, 15, 40, 40)
    
    edges = cv.Canny(gray_blur, thresLow, thresHi)
    edges2 = cv.Canny(gray_blur2, thresLow, thresHi)
    
    cv.imshow("Canny edge 2", edges2)
    cv.imshow("Canny edge", edges)


# Create window
windowName = 'Canny edge detection'
cv.namedWindow(windowName)
cv.createTrackbar('Low', windowName, 0, thresLowMax, trackbar_low_callback)
cv.createTrackbar('High', windowName, thresLowMax, thresHighMax, trackbar_high_callback)

trackbar_high_callback(thresHi)
trackbar_low_callback(thresLow)

if cv.waitKey() == ord('q'):
    cv.destroyAllWindows()
