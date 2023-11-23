from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse

window = "corner detection"


# arguments
parser = argparse.ArgumentParser()
parser.add_argument('input', type=str)
args = parser.parse_args()


# load source image
src = cv.imread(args.input)
if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)
    
    
def detect_corner(src, thresh, block_size=2, ksize=3, k=0.04):
    src_copy = src.copy()
    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    
    # Detect corners
    dst = cv.cornerHarris(src_gray, block_size, ksize, k)
    dilated_dst = cv.dilate(dst, None)
    
    src_copy[dilated_dst > thresh/1000 * dilated_dst.max()] = [0, 0, 255]
    
    # Display results
    cv.imshow(window, src_copy)



def on_trackbar(val):
    detect_corner(src, val)



if __name__ == "__main__":

    # create window
    cv.namedWindow(window)
    
    # create trackbar
    default_thresh = 50
    max_thresh = 100
    cv.createTrackbar('Threshold', window, default_thresh, max_thresh, on_trackbar)
    
    # detect corners
    detect_corner(src, default_thresh)
    
    if cv.waitKey() == ord('q'):
        cv.destroyAllWindows()
