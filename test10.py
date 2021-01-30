import cv2
import numpy as np

def nothing(x):  # 滑动条的回调函数
    pass

img = cv2.imread('../image/test32.jpg', 0)
cv2.imshow('image1',img)
edges = cv2.Canny(img, 50, 100)
cv2.namedWindow('image')
cv2.createTrackbar('mininterval', image, 0, 255, nothing)
cv2.createTrackbar('maxinterval', image, 0, 255, nothing) 

while(1):
    cv2.imshow('image', edges)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break


cv2.destroyAllWindows()



