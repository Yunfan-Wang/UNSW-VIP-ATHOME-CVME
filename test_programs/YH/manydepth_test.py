import cv2
import numpy as np
import matplotlib.pyplot as plt
from manydepth import manydepth

    
cap = cv2.VideoCapture(0)
m = manydepth()

plt.ion()
plt.show(block=True)

ax1 = plt.subplot(1,2,1)
ax2 = plt.subplot(1,2,2)

old_ret, old_frame = ret, frame = cap.read()

while (True):
    try:
        ret, frame = cap.read()
        depth = m.eval(frame, old_frame)
        
        ax1.imshow(frame)
        ax2.imshow(depth)

        old_ret, old_frame = ret, frame

        plt.pause(0.01)
        
    except Exception as e:
        print(e)
        break

plt.show()

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()