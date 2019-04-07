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
startCase = np.empty((res[0],res[1],3), dtype = np.uint32)
endCase = np.empty((res[0],res[1],1), dtype = np.uint32)
delta = 0

last_frame = []
sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format = 'bgr', use_video_port = True):
    image = frame.array
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    try:
        delta = cv2.subtract(endCase, image)
    except:
        delta = delta
        print('error')


    cv2.imshow("current_state", delta)
    endCase = image
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    if(key) == ord("q"):
        break
