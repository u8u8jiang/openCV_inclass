import cv2
import numpy as np
from matplotlib import pyplot as plt

src = cv2.imread('../image/test21_1.jpg')
img = src.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #灰階
ret, thresh = cv2.threshold(imgray, 127, 255, 0) #threshold
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cnt = contours[0]   #contours輪廓
draw = cv2.drawContours(img, cnt, -1, (0, 255, 0), 10)

plt.subplot(121), plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB)), plt.title('Src')
plt.subplot(122), plt.imshow(cv2.cvtColor(draw, cv2.COLOR_BGR2RGB)), plt.title('image')
plt.show()

