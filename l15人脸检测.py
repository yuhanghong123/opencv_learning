import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread("curry.jpg")
plt.imshow(img[:, :, ::-1])
# plt.show()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

face_cas = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
face_cas.load('haarcascade_frontalface_default.xml')
eyes_cas = cv.CascadeClassifier("haarcascade_eye.xml")
eyes_cas.load('haarcascade_eye.xml')

# 人脸检测
face_rects = face_cas.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
# 绘制人脸检测眼睛
for facerect in face_rects:
    x, y, w, h = facerect
    cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
    roi_color = img[y:y + h, x:x + w]
    roi_gray = gray[y:y + h, x:x + w]
    eyes = eyes_cas.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 3)
plt.imshow(img[:,:,::-1])
plt.show()
