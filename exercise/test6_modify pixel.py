import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('albert.jpg',1)
b = cv2.imread('albert.jpg',1)
#圖像拆分
b[2250:2400,180:1500,0]=0   #B
b[2250:2400,180:1500,1]=0   #G綠
# b[2250:2400,200:1500,2]=0   #R藍
# print(b)

cv2.namedWindow('albert',cv2.WINDOW_NORMAL)
cv2.imshow('albert',img)
cv2.namedWindow('b',cv2.WINDOW_NORMAL)
cv2.imshow('b',b)

cv2.waitKey(0)
cv2.destroyAllWindows()