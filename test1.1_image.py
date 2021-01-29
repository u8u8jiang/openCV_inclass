import cv2 
import numpy as np

img=cv2.imread('albert.jpg',0) 
#　can change the term to number，
# cv2.IMREAD_GRAYSCALE=0，cv2.IMREAD_COLOR=1


cv2.namedWindow('albert.jpg',cv2.WINDOW_NORMAL) # prevent the window too big 
cv2.imshow('albert.jpg',img) 
cv2.imwrite('albert1.jpg',img)  #store picture, can transfer color to black-white 
cv2.waitKey(0)
cv2.destoryAllWindows()