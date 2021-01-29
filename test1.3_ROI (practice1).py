# ROI practice

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('albert.jpg',1)
# img[100,100] = [0,0,0]
# print(img.shape)
roi = img[1171:1466,669:1012]
img[237:532,1045:1388] = roi

img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img1) 
plt.xticks([]), plt.yticks([]) 
plt.show()

