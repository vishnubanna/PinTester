import wiringpi2 as wiringpi
#import wp as wiringpi
from time import sleep
import picamera
import cv2
import numpy as np
import time
import pycamera.array
from picamera import PiCamera
import os

def automatic():
  wiringpi.wiringPiSetupGpio()
  wiringpi.pinMode(17, 1)
  wiringpi.pinMode(27, 1)
  wiringpi.pinMode(22, 1)
  wiringpi.pinMode(5, 1)
  wiringpi.pinMode(6, 1)

  width = 640
  length = 480
  cycles = 1000
  region = width/5
  lenreg = length/4

  camera = PiCamera()
  camera.resolution = (width,length)
  camera.framerate = 20
  rawCapture = PiRGBArray(camera, size = (width,length))

  startCase = np.empty((width,length,3), dtype = np.uint32)
  endCase = np.empty((width,length,3), dtype = np.uint32)
  delta = np.empty((width,length,1), dtype = np.uint8)
  time.sleep(0.1)
  roi1 = []
  roi2 = []
  roi3 = []
  roi4 = []
  roi5 = []

  input = raw_input("run y/n")
  if input == "y":
    run = 0
    wiringpi.digitalWrite(17, 0)
    wiringpi.digitalWrite(27, 0)
    wiringpi.digitalWrite(22, 0)
    wiringpi.digitalWrite(5, 0)
    wiringpi.digitalWrite(6, 0)
    print("running {} cycles on all pins".format(cycles))
    while (run < cylces):
      try:
        with PiCamera() as pcam:
            pcam.capture(startCase, 'rgb')
            sleep(0.001)
            pcam.start_recording('test.mp4')
        wiringpi.digitalWrite(17, 1)
        sleep(0.004)
        wiringpi.digitalWrite(27, 1)
        sleep(0.004)
        wiringpi.digitalWrite(22, 1)
        sleep(0.004)
        wiringpi.digitalWrite(5, 1)
        sleep(0.004)
        wiringpi.digitalWrite(6, 1)
        sleep(0.004)
        wiringpi.digitalWrite(17, 0)
        sleep(0.004)
        wiringpi.digitalWrite(27, 0)
        sleep(0.004)
        wiringpi.digitalWrite(22, 0)
        sleep(0.004)
        wiringpi.digitalWrite(5, 0)
        sleep(0.004)
        wiringpi.digitalWrite(6, 0)
        print("HIGH")
        sleep(2)
        wiringpi.digitalWrite(17, 1)
        sleep(0.004)
        wiringpi.digitalWrite(27, 1)
        sleep(0.004)
        wiringpi.digitalWrite(22, 1)
        sleep(0.004)
        wiringpi.digitalWrite(5, 1)
        sleep(0.004)
        wiringpi.digitalWrite(6, 1)
        sleep(0.004)
        wiringpi.digitalWrite(17, 0)
        sleep(0.004)
        wiringpi.digitalWrite(27, 0)
        sleep(0.004)
        wiringpi.digitalWrite(22, 0)
        sleep(0.004)
        wiringpi.digitalWrite(5, 0)
        sleep(0.004)
        wiringpi.digitalWrite(6, 0)
        print("LOW")
        sleep(0.004)

        with PiCamera() as pcam:
            pcam.stop_recording('test.mp4')
            pcam.capture(endCase, 'rgb')

        startCase = cv2.cvtColor(startCase, cv2.COLOR_BGR2GRAY)
        endCase = cv2.cvtColor(endCase, cv2.COLOR_BGR2GRAY)
        delta = cv2.subtract(startCase, endCase)
        roi1 = delta[0:(region), 2*lenreg:(3*lenreg)]
        roi2 = delta[(region):(2*region), 2*lenreg:(3*lenreg)]
        roi3 = delta[(2*region):(3*region), 2*lenreg:(3*lenreg)]
        roi4 = delta[(3*region):(4*region), 2*lenreg:(3*lenreg)]
        roi5 = delta[(4*region):(width), 2*lenreg:(3*lenreg)]

        #avg = np.average(np.asarray(delta))
        r1avg = np.average(np.asarray(roi1))
        r2avg = np.average(np.asarray(roi2))
        r3avg = np.average(np.asarray(roi3))
        r4avg = np.average(np.asarray(roi4))
        r5avg = np.average(np.asarray(roi5))

        run = pinfail(1, r1avg, run, cycles)
        run = pinfail(2, r2avg, run, cycles)
        run = pinfail(3, r3avg, run, cycles)
        run = pinfail(4, r4avg, run, cycles)
        run = pinfail(5, r5avg, run, cycles)

        run = run + 1

      except KeyboardInterrupt:
        run = cylces
        wiringpi.digitalWrite(17, 0)
        wiringpi.digitalWrite(27, 0)
        wiringpi.digitalWrite(22, 0)
        wiringpi.digitalWrite(5, 0)
        wiringpi.digitalWrite(6, 0)
        sleep(1)
        print("User ended premature")
        return


def pinfail(num, ravg, run, cycles):
    if (ravg > 1):
        print("pin in region {} has failed, region avg: {}".format(num, ravg))
        run = cylces
        wiringpi.digitalWrite(17, 0)
        wiringpi.digitalWrite(27, 0)
        wiringpi.digitalWrite(22, 0)
        wiringpi.digitalWrite(5, 0)
        wiringpi.digitalWrite(6, 0)
        sleep(1)
        print("failure ended premature")
    return run
