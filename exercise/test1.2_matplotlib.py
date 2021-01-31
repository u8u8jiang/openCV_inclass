import cv2
import numpy as np
from matplotlib import pyplot as plt

# import an image
img = cv2.imread('albert.jpg',1)
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)   #turn bgr to rgb #(R,G,B) each term is 0~255, 0(black)~255(white)

# use matplotlib transfer image, the pros is there is a bosrd to adjust directly
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()

