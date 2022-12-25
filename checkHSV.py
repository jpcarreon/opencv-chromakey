import cv2 as cv
import numpy as np
import os

def zeroPad(num, padding = 4):
    retVal = str(num)
    for _ in range(len(retVal), padding):
        retVal = "0" + retVal
    
    return retVal

def nothing(): pass

video = cv.VideoCapture("main.mp4")
image = cv.imread("./bg.jpg")

cv.namedWindow("Trackbars")
cv.resizeWindow("Trackbars", 300, 300)

defaultValues = {
    "lower": [29, 169, 48],
    "upper": [66, 255, 249]
}

cv.createTrackbar("L-H", "Trackbars", defaultValues["lower"][0], 179, nothing)
cv.createTrackbar("L-S", "Trackbars", defaultValues["lower"][1], 255, nothing)
cv.createTrackbar("L-V", "Trackbars", defaultValues["lower"][2], 255, nothing)
cv.createTrackbar("U-H", "Trackbars", defaultValues["upper"][0], 179, nothing)
cv.createTrackbar("U-S", "Trackbars", defaultValues["upper"][1], 255, nothing)
cv.createTrackbar("U-V", "Trackbars", defaultValues["upper"][2], 255, nothing)

while True:
    ret, frame = video.read()
    if ret:
        frame = cv.resize(frame, (640, 480))
        image = cv.resize(image, (640, 480))

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        l_h = cv.getTrackbarPos("L-H", "Trackbars")
        l_s = cv.getTrackbarPos("L-S", "Trackbars")
        l_v = cv.getTrackbarPos("L-V", "Trackbars")
        u_h = cv.getTrackbarPos("U-H", "Trackbars")
        u_s = cv.getTrackbarPos("U-S", "Trackbars")
        u_v = cv.getTrackbarPos("U-V", "Trackbars")

        l_green = np.array([l_h, l_s, l_v])
        u_green = np.array([u_h, u_s, u_v])

        mask = cv.inRange(hsv, l_green, u_green)
        res = cv.bitwise_and(frame, frame, mask=mask)
        f = frame - res
        f = np.where(f == 0, image, f)
        

        cv.imshow("video", frame)
        cv.imshow("mask", mask)
        cv.imshow("final", f)
    else:
        video.set(cv.CAP_PROP_POS_FRAMES, 0)
        continue

    if cv.waitKey(25) == 27:
        break

video.release()
cv.destroyAllWindows()

print([l_h, l_s, l_v])
print([u_h, u_s, u_v])


