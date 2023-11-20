#Testing thresholding camera input

import cv2 as cv
import numpy as np

#Initialise Video Capture device
cap = cv.VideoCapture(1)

#load cascade from data folder
faceCascade = cv.CascadeClassifier('./data/facecascade_haar.xml')

while True:
  
  #Read in a fram
  ret, frame = cap.read()
  
  #Exit on failure to open capture device
  if not ret:
    print('Camera could not open')
    break
  
  #Get properties of frame
  width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
  height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
  
  #Create a blank image to put smaller frames onto -> resize the reference frame to be a quarter of the size
  img = np.zeros((height, width), np.uint8)
  frameSmall = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)
  
  #Convert the resized frame to grayscale for use
  gray = cv.cvtColor(frameSmall, cv.COLOR_BGR2GRAY)
  
  #Apply different thresholds to frames
  ret, thresholded1 = cv.threshold(gray, 100, 200, cv.THRESH_BINARY)
  thresholded2 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 3)
  thresholded3 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 17, 5)  
  
  #Paste in all 4 frames into the blank canvas
  img[:height//2, :width//2] = gray
  img[height//2:, :width//2] = thresholded1
  img[:height//2, width//2:] = thresholded2
  img[height//2:, width//2:] = thresholded3
  
  #Run face and corner detection
  faces = faceCascade.detectMultiScale(img, 1.1, 4)
  corners = cv.goodFeaturesToTrack(img, 40, 0.01, 40)
  
  #Convert to proper type for display
  corners = np.int0(corners)
  
  #Convert back to 3 channels for coloured rectangles / circles
  img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
  
  #Add rectangles to detected face coordinates
  for (x, y, w, h) in faces:
        cv.rectangle(img, pt1=(x,y), pt2=(x + w, y + h), color=(150, 0, 200), thickness=3)
        
  #Add circles to detected corner coordinates
  for corner in corners:
    arr = corner.ravel()
    x, y = arr[0], arr[1]
    cv.circle(img, center=(x, y), radius=5, color=(0,0,255), thickness=-1)
    
  #Show the image
  cv.imshow('Adaptive thresholding (Gaussian)', img)
  
  #Quit on pressing 'q'
  if cv.waitKey(1) == ord('q'):
    break
  
#Release camera and destroy the windows
cap.release()
cv.destroyAllWindows()



