import wiringpi2 as wiringpi
#import wp as wiringpi
from time import sleep
import numpy as np
import time
import os

def automatic():
    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(17, 1)
    wiringpi.pinMode(27, 1)
    wiringpi.pinMode(22, 1)
    wiringpi.pinMode(5, 1)
    wiringpi.pinMode(6, 1)

    TIMECONSTANT = 0.004
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
                wiringpi.digitalWrite(17, 1)
                sleep(TIMECONSTANT)
                wiringpi.digitalWrite(27, 1)
                sleep(TIMECONSTANT)
                wiringpi.digitalWrite(22, 1)
                sleep(TIMECONSTANT)
                wiringpi.digitalWrite(5, 1)
                sleep(TIMECONSTANT)
                wiringpi.digitalWrite(6, 1)
                sleep(TIMECONSTANT)
                wiringpi.digitalWrite(17, 0)
                sleep(TIMECONSTANT)
                wiringpi.digitalWrite(27, 0)
                sleep(TIMECONSTANT)
                wiringpi.digitalWrite(22, 0)
                sleep(TIMECONSTANT)
                wiringpi.digitalWrite(5, 0)
                sleep(TIMECONSTANT)
                wiringpi.digitalWrite(6, 0)
                print("HIGH")
                sleep(2)
                wiringpi.digitalWrite(17, 1)
                sleep(TIMECONSTANT)
                wiringpi.digitalWrite(27, 1)
                sleep(TIMECONSTANT)
                wiringpi.digitalWrite(22, 1)
                sleep(TIMECONSTANT)
                wiringpi.digitalWrite(5, 1)
                sleep(TIMECONSTANT)
                wiringpi.digitalWrite(6, 1)
                sleep(TIMECONSTANT)
                wiringpi.digitalWrite(17, 0)
                sleep(TIMECONSTANT)
                wiringpi.digitalWrite(27, 0)
                sleep(TIMECONSTANT)
                wiringpi.digitalWrite(22, 0)
                sleep(TIMECONSTANT)
                wiringpi.digitalWrite(5, 0)
                sleep(TIMECONSTANT)
                wiringpi.digitalWrite(6, 0)
                print("LOW")
                sleep(TIMECONSTANT)
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

if __name__ == "__main__":
    automatic() 
