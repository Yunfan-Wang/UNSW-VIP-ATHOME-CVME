# Detecting different coloured lines
import cv2 as cv
import numpy as np

# Load the image
image = cv.imread('Colours.png')

# Define the lower and upper bounds for blue color in BGR format
lower_blue = np.array([100, 0, 0])  # Adjust these values to match your specific shade of blue
upper_blue = np.array([255, 110, 110])  # Adjust these values as needed

# Create a mask that selects pixels within the blue color range
blue_mask = cv.inRange(image, lower_blue, upper_blue)

# Apply the mask to the original image to extract the blue portions
blue_portion = cv.bitwise_and(image, image, mask=blue_mask)

# Display the blue portion of the image
cv.imshow("Mask", blue_mask)
cv.imshow('Blue Portion', blue_portion)
cv.waitKey(0)
cv.destroyAllWindows()
