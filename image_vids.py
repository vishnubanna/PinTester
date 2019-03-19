import cv2
import numpy as np
import time
import pycamera.array
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (640,480)
camera.imgrate = 20
rawCapture = PiRGBArray(camera, size = (640,480))

time.sleep(0.1)
#vid = cv2.VideoCapture('testp.mp4')
cap = cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
past_img = []
#while True:
for frame in camera.capture_continuous(rawCapture, format = "bgr", use_video_port = True)
    #time.sleep(0.3)
    #ret, img = cap.read()

    img = frame.array

    cv2.imshow('img', img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    try:
        delta = cv2.subtract(past_img, gray)
    except:
        delta = gray
    past_img = gray
    cv2.imshow('gray', delta)
    #out.write(img)
    art = np.asarray(delta)
    total = 0
    avg = np.average(art)
    rawCapture.truncate(0)
    if (avg > 1):
        print(avg, "motion detected")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
#out.release()
cap.destroyAllWindows()
