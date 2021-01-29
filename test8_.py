import cv2
import numpy as np

# # 13.1 RGB to HSV
# flag = [i for i in dir(cv2) if i.startswith('COLOR_')]
# print(flags)
# cv2.cvtColor
# cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

# 13.2 
cap=cv2.VideoCapture(0)
while(1):
#获取每一帧 
    ret,frame=cap.read()
        
#换到HSV 
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_blue=np.array([0,50,50]) #定蓝色的值，調整抓不同顏色，光影有雜訊 ex.白色打到是0
    upper_blue=np.array([10,255,255])

    cv2.resize

    mask=cv2.inRange(hsv,lower_blue,upper_blue)  #根据值构建掩模 
    res=cv2.bitwise_and(frame,frame,mask=mask) #对原图像和掩模位算(abc圖做and)
#显示图像 
    cv2.imshow('frame',frame) 
    cv2.imshow('mask',mask) 
    cv2.imshow('res',res) 
    k=cv2.waitKey(5)&0xFF 
    if k==27: 
        break
#关窗口 
cv2.destroyAllWindows()





