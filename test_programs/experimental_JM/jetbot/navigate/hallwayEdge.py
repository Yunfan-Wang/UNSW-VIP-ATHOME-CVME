# Navigation using hallway-floor edge detection

import cv2 as cv
import numpy as np

# initialise video capture device
cap = cv.VideoCapture(0)

# initialise Canny thresholds
thresHigh = 150
thresLow = 100

# Scans the horizantal contact boundary and finds the point of intersection with the largest Canny detected edge
def scanLine(edges, width, boundary):
    for i in range(width):
        if edges[boundary][i] == 1:
            cv.circle(edges, (boundary, i), 10, (0,255,0), -1)
        
    return edges

# Enter loop
while True:
    # Get frame and dimensions
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    # Initiate boundary of contact
    boundary_top = int(np.floor(3*height/4))
    
    # Apply threshold to image for edge detection
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray_blur = cv.bilateralFilter(gray, 10, 40, 40)
    edges = cv.Canny(gray_blur, thresLow, thresHigh)
    
    # Find points of intersection
    edges = scanLine(edges, width, boundary_top)
    cv.cvtColor(edges, cv.COLOR_GRAY2BGR)
    
    # Visualise contact boundary
    cv.line(edges, (0, boundary_top), (width - 1, boundary_top), (255, 0, 0), 3)
    
    # Apply Hough line transform to detect long edge
    lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=width/4, maxLineGap=350)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(edges, (x1, y1), (x2, y2), (255, 0, 0), 3)

    cv.imshow("Edges", edges)
    
    if cv.waitKey(1) == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()