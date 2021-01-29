

import cv2 
import numpy as np


def nothing(x): 
    pass
# build a colorful board
img=np.zeros((300,512,3),np.uint8) 
cv2.namedWindow('image')

cv2.createTrackbar('R','image',0,255,nothing) 
cv2.createTrackbar('G','image',0,255,nothing) 
cv2.createTrackbar('B','image',0,255,nothing)

switch='0:OFF\n1:ON' 
cv2.createTrackbar(switch,'image',0,1,nothing)

while(1): 
    cv2.imshow('image',img) 
    k=cv2.waitKey(1)&0xFF 
    if k==27: 
        break
    r=cv2.getTrackbarPos('R','image') 
    g=cv2.getTrackbarPos('G','image') 
    b=cv2.getTrackbarPos('B','image') 
    s=cv2.getTrackbarPos(switch,'image')

if s==0: 
    img[:]=[255,255,255]   #defult is white 
else: 
    img[:]=[b,g,r]

cv2.destroyAllWindows()