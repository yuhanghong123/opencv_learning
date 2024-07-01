import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# create image
img = np.zeros((512, 512, 3), np.uint8)

# draw image
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv.circle(img, (256, 256), 60, (0, 0, 255), 4)
cv.rectangle(img, (100, 100), (400, 400), (0, 255, 0), 5)
cv.putText(img,'the second class of opencv',(30,30),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),3)
# show image
plt.imshow(img[:, :, ::-1])
plt.show()
