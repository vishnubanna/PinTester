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

def pinfail(num, ravg, fails, cycles):
    if (ravg > 1):
        print("pin in region {} has possibly  failed, region avg: {}".format(num, ravg))
        fails = fails + 1
        wiringpi.digitalWrite(17, 0)
        wiringpi.digitalWrite(27, 0)
        wiringpi.digitalWrite(22, 0)
        wiringpi.digitalWrite(5, 0)
        wiringpi.digitalWrite(6, 0)
        sleep(1)
    return fails


wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(17, 1)
wiringpi.pinMode(27, 1)
wiringpi.pinMode(22, 1)
wiringpi.pinMode(5, 1)
wiringpi.pinMode(6, 1)

width = 640
length = 480
cycles = 1000

TIMECONSTANT = 0.004

region = width/5
lenreg = length/4
failCounter = 0

camera = PiCamera()
camera.resolution = (width,length)
camera.framerate = 20
rawCapture = PiRGBArray(camera, size = (width,length))

startCase = np.empty((width,length,3), dtype = np.uint32)
endCase = np.empty((width,length,3), dtype = np.uint32)
delta = []
time.sleep(0.1)
roi1 = []
roi2 = []
roi3 = []
roi4 = []
roi5 = []

print("running {} cycles on all pins".format(cycles))

input = raw_input("run y/n")
if input == "y":
  run = 0
  wiringpi.digitalWrite(17, 0)
  wiringpi.digitalWrite(27, 0)
  wiringpi.digitalWrite(22, 0)
  wiringpi.digitalWrite(5, 0)
  wiringpi.digitalWrite(6, 0)
  print("running {} cycles on all pins".format(cycles))


while (run < cycles):
    try:
        with PiCamera() as pcam:
            pcam.capture(startCase, 'rgb')
            sleep(0.001)
            pcam.start_recording('test.mp4')

        for i in range(0, 5):
            sleep(1)
            print("i am recording {}".format(i))

        with PiCamera() as pcam:
            pcam.stop_recording('test.mp4')
            sleep(0.01)
            pcam.capture(endCase, 'rgb')

        startCase = cv2.cvtColor(startCase, cv2.COLOR_BGR2GRAY)
        endCase = cv2.cvtColor(endCase, cv2.COLOR_BGR2GRAY)

        delta = cv2.subtract(startCase, endCase)
        cv2.imshow('delta', delta)


        delta = np.asarray(delta)

        roi1 = delta[0:(region), 2*lenreg:(3*lenreg)]
        roi2 = delta[(region):(2*region), 2*lenreg:(3*lenreg)]
        roi3 = delta[(2*region):(3*region), 2*lenreg:(3*lenreg)]
        roi4 = delta[(3*region):(4*region), 2*lenreg:(3*lenreg)]
        roi5 = delta[(4*region):(width), 2*lenreg:(3*lenreg)]

        r1avg = np.average(np.asarray(roi1))
        r2avg = np.average(np.asarray(roi2))
        r3avg = np.average(np.asarray(roi3))
        r4avg = np.average(np.asarray(roi4))
        r5avg = np.average(np.asarray(roi5))

        failCounter = pinfail(1, r1avg, failCounter, cycles)
        failCounter = pinfail(2, r2avg, failCounter, cycles)
        failCounter = pinfail(3, r3avg, failCounter, cycles)
        failCounter = pinfail(4, r4avg, failCounter, cycles)
        failCounter = pinfail(5, r5avg, failCounter, cycles)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if failCounter > 5:
            runs = cycles
            print("failure ended premature")

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
        
