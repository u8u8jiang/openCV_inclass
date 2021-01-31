import cv2
import numpy as np
from matplotlib import pyplot as plt

######################################################
######## type "orvid" to show code directly #########
#######################################################

#Import only if not previously imported

# Create a Video Reader Object.
cap = cv2.VideoCapture(0)  #the number of carema
if cap.isOpened() == False:
    print("Error in opening video stream or file")

#Define the codec for the Video
fourcc = cv2.VideoWriter_fourcc(*'XVID')  #設定編碼方式
#Create Video Writer Object
writer = cv2.VideoWriter('test.avi',fourcc, 30, (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # writer.write(frame)
        cv2.imshow("Frame",frame) #desplay the frame
        # Exit on pressing esc
        if cv2.waitKey(20) & 0xFF == 27:
            break
    else:
        break
cap.release()
writer.release()
cv2.destroyAllWindows()