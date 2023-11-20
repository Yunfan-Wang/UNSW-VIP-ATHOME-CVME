# run vision program

import cv2 as cv
import numpy as np
from vision import Vision
import math

# Initialise vision module
Observer = Vision()

# initialise video capture
img = cv.imread("testGround.jpg")

height, width, c = img.shape

# End of stream
if img is None:
    exit();

# Single image
ret = Observer.findVanishingPoint(img)
    
x, y, lines = ret
if math.isnan(x) or math.isnan(y):
    exit();

# Figure out course of movement from here
cmd = Observer.chooseMovement(img, x, y)

# Then do something based on this command

############################
# VISUALISING #
############################

# Visualise boundaries
boundary_left = int(np.round(width/2 - width/16))
boundary_right = int(np.round(width/2 + width/16))
print(boundary_left, boundary_right)

# Left line
cv.line(img, (boundary_left, 0), (boundary_left, height - 1), (0, 255, 0), 3)
#Right Line
cv.line(img, (boundary_right, 0), (boundary_right, height - 1), (0, 255, 0), 3)

# Purely for visual purpose
for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
        
# Visualise Vanishing Point
newImg = cv.circle(img, center=(int(np.round(x)), int(np.round(y))), radius=10, color=(0, 200, 0), thickness=-1)
newImg = cv.putText(newImg, cmd, org=(100,100), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=10, color=(0,0,255), thickness=3)

cv.imshow('VP', newImg)

if cv.waitKey() == ord('q'):
    cv.destroyAllWindows()