
# ROI practice

# import an image
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('albert.jpg',1)
# can change the term to number
# cv2.IMREAD_GRAYSCALE=0
# cv2.IMREAD_COLOR=1
roi = img[77:122,640:780]
img[149:194,460:600] = roi

img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)   #0(black)~255(white) #(R,G,B) each term is 0~255
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.imshow(img1)
plt.xticks([]), plt.yticks([])
plt.show()

#add the word on the graph
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img1,'text',(100,100),font,2,(255,255,255),5)







img[100,100] = [0,0,0]
print(img.shape,img.size)

x = txt.capitalize()


# cv2.namedWindow('albert.jpg',cv2.WINDOW_NORMAL) # prevent the window too big 
# cv2.imshow('albert.jpg',img) 
# cv2.imwrite('albert1.jpg',img)  #store picture, can transfer color to black-white 
# cv2.waitKey(0)
# cv2.destoryAllWindows()
