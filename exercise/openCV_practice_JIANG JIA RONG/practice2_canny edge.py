import cv2
import numpy as np

def nothing(x):  # 滑动条的回调函数
    pass

img = cv2.imread('albertadult.jpg',0)
cv2.imshow('image_original',img)

edges = cv2.Canny(img, 50, 100)
cv2.namedWindow('image_canny')
cv2.createTrackbar('minval', 'image_canny', 0, 255, nothing)
cv2.createTrackbar('maxval', 'image_canny', 0, 255, nothing) 
while(1):
    cv2.imshow('image_canny', edges)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    minval = cv2.getTrackbarPos('minval','image_canny')
    maxval = cv2.getTrackbarPos('maxval','image_canny')
    edges = cv2.Canny(img, minval, maxval)

cv2.destroyAllWindows()



