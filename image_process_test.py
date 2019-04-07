from picamera.array import PiRGBArray
from picamera import PiCamera
from time import*
import cv2
import numpy as np

res = (640, 480)
camera = PiCamera()
camera.resolution = (res[0], res[1])
camera.framerate = 15
rawCapture = PiRGBArray(camera, size = (res[0], res[1]))

last_frame = []
sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format = 'bgr', use_video_port = True):
    #image = np.asarray(frame)
    #pic = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow("current_state", frame)
    key = cv2.waitKey(q) & 0xFF

    rawCapture.truncate(0)

    if(key) == ord("q"):
        break
