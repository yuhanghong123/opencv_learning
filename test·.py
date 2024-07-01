import cv2 as cv
import matplotlib.pyplot as plt
import numpy

img = cv.imread("test.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret ,thresh = cv.threshold(gray,120,255,cv.THRESH_BINARY)

plt.imshow(thresh,cmap=plt.cm.gray)
plt.show()

contours,hierarchy =cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
draw_img = img.copy()
res = cv.drawContours(draw_img,contours,2,(255,0,0),1)

plt.imshow(res[:,:,::-1])
plt.show()
