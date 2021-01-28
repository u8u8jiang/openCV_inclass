import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
cv2.line(img,(0,0),(500,500), (255,0,0),5)   #line
cv2.rectangle(img,(100,100),(300,300),(0,255,0),3) #tangle
cv2.circle(img,(200,200),150,(100,100,100),5)
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# five-vertex 
points = np.array([[200,200],[300,100],[400,200],[400,400],[200,400]],np.int32)
print(points)    
# import only if not previously imported
cv2.polylines(img,[points],True,(0,0,100),5)

#add the word on the graph
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'text',(100,100),font,2,(255,255,255),5)

#
# #mouse callback function
# def draw_circle(event,x,y,flags,param): 
#     if event == cv2.EVENT_LBUTTONDBLCLK: 
#         cv2.circle(img,(x,y),100,(255,0,0),-1)

# #创建图像与窗口并将窗口与回函数绑定 
# img=np.zeros((512,512,3),np.uint8) 
# cv2.namedWindow('image') 
# cv2.setMouseCallback('image',draw_circle)

# while(1): 
#     cv2.imshow('image',img) 
#     if cv2.waitKey(20) & 0xFF == 27: 
#         break 
#     cv2.destroyAllWindows()



cv2.imshow('window name', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

