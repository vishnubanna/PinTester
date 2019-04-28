import wiringpi2 as wiringpi
#import wp as wiringpi
from time import sleep
import picamera
import cv2
import numpy as np
import time
import picamera.array
from picamera import PiCamera

def automatic():
    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(17, 1)
    wiringpi.pinMode(27, 1)
    wiringpi.pinMode(22, 1)
    wiringpi.pinMode(5, 1)
    wiringpi.pinMode(6, 1)

    timeLen = 0.004

    input = raw_input("run y/n")

    if input == "y":
        run = 0
        wiringpi.digitalWrite(17, 0)
        wiringpi.digitalWrite(27, 0)
        wiringpi.digitalWrite(22, 0)
        wiringpi.digitalWrite(5, 0)
        wiringpi.digitalWrite(6, 0)
        print("running 10000 cycles on all pins")


        camera = PiCamera()

        camera.resolution = (640,480)
        camera.framerate = 20

        camera.start_recording('test_no_fail_detection.h264')
        camera.start_preview()

        cycles = 10000

        while (run < cycles):
            try:
                wiringpi.digitalWrite(17, 1)
                sleep(timeLen)
                wiringpi.digitalWrite(27, 1)
                sleep(timeLen)
                wiringpi.digitalWrite(22, 1)
                sleep(timeLen)
                wiringpi.digitalWrite(5, 1)
                sleep(timeLen)
                wiringpi.digitalWrite(6, 1)
                print("HIGH")
                sleep(timeLen)
                wiringpi.digitalWrite(17, 0)
                sleep(timeLen)
                wiringpi.digitalWrite(27, 0)
                sleep(timeLen)
                wiringpi.digitalWrite(22, 0)
                sleep(timeLen)
                wiringpi.digitalWrite(5, 0)
                sleep(timeLen)
                wiringpi.digitalWrite(6, 0)
                print("LOW")
                sleep(2)
                wiringpi.digitalWrite(17, 1)
                sleep(timeLen)
                wiringpi.digitalWrite(27, 1)
                sleep(timeLen)
                wiringpi.digitalWrite(22, 1)
                sleep(timeLen)
                wiringpi.digitalWrite(5, 1)
                sleep(timeLen)
                wiringpi.digitalWrite(6, 1)
                print("HIGH")
                sleep(timeLen)
                wiringpi.digitalWrite(17, 0)
                sleep(timeLen)
                wiringpi.digitalWrite(27, 0)
                sleep(timeLen)
                wiringpi.digitalWrite(22, 0)
                sleep(timeLen)
                wiringpi.digitalWrite(5, 0)
                sleep(timeLen)
                wiringpi.digitalWrite(6, 0)
                print("LOW")
                sleep(timeLen)
            except KeyboardInterrupt:
                run = cycles
                wiringpi.digitalWrite(17, 0)
                wiringpi.digitalWrite(27, 0)
                wiringpi.digitalWrite(22, 0)
                wiringpi.digitalWrite(5, 0)
                wiringpi.digitalWrite(6, 0)
                sleep(1)
                print("User ended premature")

        camera.stop_recording()
        camera.stop_preview()
        return

if __name__ == "__main__":
    automatic()
