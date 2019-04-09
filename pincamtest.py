import wiringpi2 as wiringpi
#import wp as wiringpi
from time import sleep
import picamera
import cv2
import numpy as np
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
import os

def pinfail(num, ravg, fails, cycles):
    if (ravg > 10):
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


with PiCamera() as camera:
    camera.resolution = (width,length)
    camera.framerate = 20


    startCase = np.empty((width,length,3), dtype = np.uint32)
    endCase = np.empty((width,length,3), dtype = np.uint32)
    delta = []
    time.sleep(0.1)
    roi1 = []
    roi2 = []
    roi3 = []
    roi4 = []
    roi5 = []

    camera.start_recording('test.h264')
    camera.start_preview()


    while (run < cycles):
        try:
            rawCapture = PiRGBArray(camera, size = (width,length))
            rawCapture1 = PiRGBArray(camera, size = (width,length))
            with rawCapture as output:
                camera.capture(output, 'bgr')
                startCase = output.array
                if rawCapture.seekable():
                    rawCapture.seek(0)
                    rawCapture.truncate()
                else:
                    rawCapture.truncate(0)



            for i in range(0, 5):
                sleep(1)
                print("i am recording {}".format(i+1))

            with rawCapture1 as output1:
                camera.capture(output1, 'bgr')
                endCase = output1.array
                if rawCapture1.seekable():
                    rawCapture1.seek(0)
                    rawCapture1.truncate()
                else:
                    rawCapture1.truncate(0)

            startCase = cv2.cvtColor(startCase, cv2.COLOR_BGR2GRAY)
            endCase = cv2.cvtColor(endCase, cv2.COLOR_BGR2GRAY)

            delta = cv2.subtract(startCase, endCase)

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

            if failCounter > 5:
                runs = cycles
                print("failure ended premature")
                wiringpi.digitalWrite(17, 0)
                wiringpi.digitalWrite(27, 0)
                wiringpi.digitalWrite(22, 0)
                wiringpi.digitalWrite(5, 0)
                wiringpi.digitalWrite(6, 0)
                camera.stop_recording()
                camera.stop_preview()
                break

            run = run + 1

        except KeyboardInterrupt:
            run = cylces
            wiringpi.digitalWrite(17, 0)
            wiringpi.digitalWrite(27, 0)
            wiringpi.digitalWrite(22, 0)
            wiringpi.digitalWrite(5, 0)
            wiringpi.digitalWrite(6, 0)
            sleep(1)
            camers.stop_recording()
            camera.stop_preview()
            print("User ended premature")
            break
