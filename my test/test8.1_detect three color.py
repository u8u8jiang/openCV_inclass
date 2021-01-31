import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while(1):
#获取每一帧 
    ret,frame=cap.read()   
#换到HSV 
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_blue = np.array([0,50,50]) #定蓝色的值，調整抓不同顏色，光影有雜訊 ex.白色打到是0
    upper_blue = np.array([10,255,255])
    lower_red = np.array([50,0,50]) #定紅色的值，調整抓不同顏色，光影有雜訊 ex.白色打到是0
    upper_red = np.array([255,10,255])
    lower_green = np.array([50,50,0]) #定綠色的值，調整抓不同顏色，光影有雜訊 ex.白色打到是0
    upper_green = np.array([255,255,10])

    cv2.resize
#根据值构建掩模 
    mask_B = cv2.inRange(hsv,lower_blue,upper_blue)
    mask_R = cv2.inRange(hsv,lower_red,upper_red)
    mask_G = cv2.inRange(hsv,lower_green,upper_green)
    mask = cv2.add(mask_B,mask_R,mask_G)
#对原图像和掩模位算(abc圖做and)     
    res_B = cv2.bitwise_and(frame,frame,mask=mask_B) 
    res_R = cv2.bitwise_and(frame,frame,mask=mask_R) 
    res_G = cv2.bitwise_and(frame,frame,mask=mask_G) 
    res = cv2.add(res_B,res_R,res_G)
#显示图像 
    cv2.imshow('frame',frame) 
    cv2.imshow('mask',mask) 
    cv2.imshow('res',res) 
    k=cv2.waitKey(5)&0xFF 
    if k==27: 
        break
#关窗口 
cv2.destroyAllWindows()
