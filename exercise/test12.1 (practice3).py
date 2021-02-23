# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 21:32:09 2021

@author: she84
"""

# -*- coding: utf-8 -*-
"""
Creat 3*3 Gassian Kernel
"""
import numpy as np
from matplotlib import pyplot as plt
import cv2
from scipy import signal





#3*3 Gassian filter
x, y = np.mgrid[-1:2, -1:2]
gaussian_kernel = np.exp(-(x**2+y**2))

#Normalization
gaussian_kernel = gaussian_kernel / gaussian_kernel.sum()

plt.imshow(gaussian_kernel, cmap=plt.get_cmap('jet'), interpolation='nearest')
plt.colorbar()
plt.show()

"""
Convolve 3*3 Gassian Kernel with Image
"""

img = cv2.imread('testitem.jpg')
img1 = img.copy()
imgray = cv2.cvtColor(img1,cv2.COLOR_RGB2GRAY) #灰階
# blurred = signal.convolve2d(imgray, gaussian_kernel, boundary='symm', mode='same') #卷積
blurred = cv2.GaussianBlur(imgray , (11, 11), 0)  #去雜訊

#邊緣監測
edges = cv2.Canny(blurred, 20, 200)
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
draw = cv2.drawContours(img1, contours, -1, (0, 255, 0), 2)

plt.subplot(131), plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(132), plt.imshow(edges,cmap='gray'), plt.title('Edge Image')
plt.subplot(133), plt.imshow(cv2.cvtColor(draw,cv2.COLOR_BGR2RGB)), plt.title('contour Image')

plt.show()










