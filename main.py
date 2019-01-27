import wiringpi2 as wp
import math
import numpy
from time import*
import sched

def rise(pinsol, pinresis):
    wp.digitalwrite(pinsol, 0)
    wp.digitalwrite(pinresis, 1)
    sleep(1)
    wp.digitalwrite(pinsol, 1)
    wp.digitalwrite(pinresis, 0)

def lower(pinsol, pinresis, length):
    sleep(length)
    wp.digitalwrite(pinsol, 0)
    wp.digitalwrite(pinresis, 1)

#def auto():





solonoid = [17,27,22,10,9]
resis = [0,5,6,13,19]
prompt1 = "which solonoids do you want to test? enter: a number between 1 and 5, enter off to lower all"
TIME_LIMIT = 10 #seconds


wp.wiringPiSetupGpio()
wp.pinMode(solonoid[0], 1)
wp.pinMode(solonoid[1], 1)
wp.pinMode(solonoid[2], 1)
wp.pinMode(solonoid[3], 1)
wp.pinMode(solonoid[4], 1)
wp.pinMode(resis[0], 1)
wp.pinMode(resis[1], 1)
wp.pinMode(resis[2], 1)
wp.pinMode(resis[3], 1)
wp.pinMode(resis[4], 1)




choice = raw_input("would you like to control the device manually or would you like it to be automatic, m = manual a = automatic")
# inset condition to turn all pins off after l0 seconds
if choice == "m":
    m  = True
    on = []
    length = 0
    while (m):
        raised = raw_input(prompt1)
        test = raised.split(',')
        for i in range(0, len(test)):
            try:
                test[i] = int(test[i])
            except:
                test[i] = test[i]
        for i in range(0,len(test)):
            if type(test[i]) == int:
                on.append(test[i] - 1)
                rise(solonoid[test[i]-1], resis[test[i]-1])
            elif test[i] == "off":
                for j in range (0, len(solonoid)):
                    lower(solonoid[j], resis[j], length)
                m = False


elif choice == "a":
    print("working on it")
    length = raw_input("how long do you want each solonoid to be raised?")
    a = True
    try:
        while(a):
            for i in range(len(solonoid)):
                rise(solonoid[i-1], resis[i-1])
            sleep(length)
            for i in range(len(solonoid)):
                lower(solonoid[i-1], resis[i-1], 0)
    except KeyboardInterrupt:




