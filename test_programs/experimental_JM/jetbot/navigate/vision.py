# Holds class info on running detect algorithms
# Aiming to navigate using vanishing point in hallways

import cv2 as cv
import numpy as np

class Vision:
    def __init__(self):
        # initialise Canny thresholds
        self.thresHigh = 150
        self.thresLow = 100
    
    # Returns true if angle is close to zero or pi radians, and also if 
    # angle is close to pi/2 or 3pi/2 radians
    def angleUnwanted(self, angle):
        if abs(angle) < 0.09 or abs(abs(angle) - np.pi/2) < 0.09:
            return True
        return False
    
    def find_intersection(self, line1, line2):
        # extract points
        x1, y1, x2, y2 = line1[0]
        x3, y3, x4, y4 = line2[0]
        
        # compute determinant
        Px = ((x1*y2 - y1*x2)*(x3-x4) - (x1-x2)*(x3*y4 - y3*x4))/  \
            ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
        Py = ((x1*y2 - y1*x2)*(y3-y4) - (y1-y2)*(x3*y4 - y3*x4))/  \
            ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
        return Px, Py
    
    # Uses kmeans clustering to generalise position of points
    def cluster_points(self, points, nclusters):
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        _, _, centers = cv.kmeans(points, nclusters, None, criteria, 10, cv.KMEANS_PP_CENTERS)
        return centers
    
    # Finds the vanishing point of the given hallway frame
    def findVanishingPoint(self, img):
        # Get frame and dimensions
        frame = img
        height, width, c = img.shape
        
        # Initiate boundary of contact
        #boundary_top = int(np.floor(3*height/4))
        
        # Apply threshold to image for edge detection
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        gray_blur = cv.bilateralFilter(gray, 10, 40, 40)
        edges = cv.Canny(gray_blur, self.thresLow, self.thresHigh)
        
        # Apply Hough line transform to detect long edges
        lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=0, maxLineGap=50)
        lines2 = []
        
        # Remove horizantal / vertical lines
        for line in lines:
            x1, y1, x2, y2 = line[0]
            if x1 != x2:
                angle = abs(np.arctan((y2-y1)/(x2-x1)))
            else:
                angle = 0
            if not self.angleUnwanted(angle):
                lines2.append(line)
                
        # Find points of intersection
        intersections = []
        for i in range(len(lines2)):
            for j in range(i + 1, len(lines2)):
                intersect = self.find_intersection(lines2[i], lines2[j])
                
                # make sure they are in range of the image borders
                if intersect[0] > width or intersect[1] > height or intersect[0] < 0 or intersect[1] < 0:
                    continue
                
                intersections.append(intersect)
        
        intersections = np.array(intersections)
        print(intersections)
        vp_x, vp_y = 0, 0
        # Find average intersection point
        for ins in intersections:
            x, y = ins[0], ins[1]
            vp_x += x
            vp_y += y
            
        if len(intersections) is 0:
            return None
        
        vp_x /= len(intersections)
        vp_y /= len(intersections)
        return vp_x, vp_y, lines2
    
    # Based on a given vanishing point, determine the best course of action
    def chooseMovement(self, img, x, y):
        height, width, c = img.shape
        boundary_left = width/2 - width/16
        boundary_right = width/2 + width/16
        
        if x < boundary_left:
            return "L"
        if x > boundary_right:
            return "R"
        
        return "CONTINUE"