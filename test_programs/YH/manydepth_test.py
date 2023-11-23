import cv2
import numpy as np
import matplotlib.pyplot as plt
from manydepth import manydepth
import argparse

# Set up argument parser
parser = argparse.ArgumentParser()
parser.add_argument("input", type=str)
parser.add_argument('-v', '--video', action='store_true')
args = parser.parse_args()


# initialize manydepth
m = manydepth()


# image
def run_image(src):
    frame = cv2.imread(src)
    if frame is None:
        raise ValueError(f"Image not loaded correctly. Check the file path: {src}")

    depth = m.eval(frame, frame)  # Assuming manydepth can handle single images
    
    # Set up the matplotlib figure and axes
    plt.figure(figsize=(10, 5))
    ax1 = plt.subplot(1, 2, 1)
    ax2 = plt.subplot(1, 2, 2)
    
    # display image & plot
    ax1.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    ax1.set_title('Original Image')
    ax2.imshow(depth)
    ax2.set_title('Depth')
    plt.show()


# video
def run_video(src):
    cap = cv2.VideoCapture(src)
    plt.ion()
    
    # Set up the matplotlib figure and axes
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    
    # Process video frames
    ret, old_frame = cap.read()
    if not ret:
        print("Failed to read video")
        cap.release()
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        depth = m.eval(frame, old_frame)
        
        # Update plots
        ax1.clear()
        ax1.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        ax1.set_title('Original Frame')
        ax2.clear()
        ax2.imshow(depth)
        ax2.set_title('Depth')
        
        plt.pause(0.01)
        old_frame = frame

    cap.release()
    plt.close()


if __name__ == "__main__":
    input = args.input
    
    if input == "webcam":
        run_video(0)
    elif args.video:
        run_video(input)
    else:
        run_image(input)
