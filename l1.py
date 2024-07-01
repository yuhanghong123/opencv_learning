import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# read image
img = cv.imread("gege.jpg")

# show image by cv2
cv.imshow("gege", img)
cv.waitKey(0)
cv.destroyAllWindows()
# show image by matplotlib.pyplot
# plt.imshow(img[:, :, ::-1]) # 彩色
plt.imshow(img,cmap=plt.cm.gray) # 灰度
plt.show()
cv.waitKey(0)
# save image
cv.imwrite("gege.png",img)