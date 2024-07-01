import numpy as np
import cv2 as cv

# 1.read video
cap = cv.VideoCapture("cat.mov")
# 2.判断是否成功
ret ,frame = cap.read()
while (cap.isOpened()):
    # 3.获取每一帧的图像
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("frame", frame)
    if cv.waitKey(25) & 0xFF == ord("q"):
        break
cap.release()
cv.destroyAllWindows()

# width = int(cap.get(3))
# height =int(cap.get(4))
#
# out = cv.VideoWriter("out.avi",cv.VideoWriter_fourcc("M","J","P","G"),10,(width,height))
#
# while(True):
#     ret,frame = cap.read()
#     if ret==True:
#         out.write(frame)
#     else:
#         break
# cap.release()
# out.release()
# cv.destroyAllWindows()
