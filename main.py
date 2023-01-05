import cv2 as cv
import numpy as np
import os

def zeroPad(num, padding = 4):
    retVal = str(num)
    for _ in range(len(retVal), padding):
        retVal = "0" + retVal
    
    return retVal

# if set to 0, display 640x480 preview of output
finalOutput = 1
video = cv.VideoCapture("main.mp4")

# color of green screen in HSV
l_green = np.array([29, 169, 48])
u_green = np.array([66, 255, 249])

# determine number of frames to consider
frameStart = int(os.listdir("./frames/")[0][:4])
frameEnd = int(os.listdir("./frames/")[-1][:4])

if not os.path.exists("./output/"): os.mkdir("./output")

# chroma key all frames present in ./frames/ folder
for i in range(frameEnd - frameStart + 1):
    current = frameStart + i
    imageFrame = cv.imread(f"./frames/{zeroPad(current)}.jpeg")

    _, videoFrame = video.read()
    if not finalOutput:
        videoFrame = cv.resize(videoFrame, (640, 480))
        imageFrame = cv.resize(imageFrame, (640, 480))

    
    hsv = cv.cvtColor(videoFrame, cv.COLOR_BGR2HSV)

    mask = cv.inRange(hsv, l_green, u_green)
    res = cv.bitwise_and(videoFrame, videoFrame, mask=mask)

    f = videoFrame - res
    f = np.where(f == 0, imageFrame, f)

    if not finalOutput:
        cv.imshow("video", videoFrame)
        cv.imshow("mask", f)
    cv.imwrite(f"./output/{zeroPad(i)}.jpg", f)

    # ESC key
    if cv.waitKey(25) == 27: break

video.release()
cv.destroyAllWindows()

