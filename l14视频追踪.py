import numpy as np
import cv2 as cv

# 获取视频
cap = cv.VideoCapture("cat.mov")

# 指定追踪目标
ret, frame = cap.read()
r, h, c, w = 400, 200, 450,350
win = (c, r, w, h)
roi = frame[r:r + h, c:c + w]

# 计算直方图

hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
roi_hist = cv.calcHist([hsv_roi], [0], None, [100], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)

# 目标追踪
term = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)
while (True):
    ret, frame = cap.read()
    if ret == True:
        hst = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hst], [0], roi_hist, [0, 180], 1)
        ret, win = cv.meanShift(dst, win, term)
        # ret, win = cv.CamShift(dst,win,term)

        x, y, w, h = win
        img2 = cv.rectangle(frame, (x, y), (x + w, y + h), 255, 2)
        # pts = cv.boxPoints(ret)
        # pts = np.intp(pts)
        # img2 = cv.polylines(frame,[pts],True,255,2)
        cv.imshow("frame", img2)
        if cv.waitKey(60) & 0xFF== "q":
            break


# 释放资源
cap.release()
cv.destroyAllWindows()
