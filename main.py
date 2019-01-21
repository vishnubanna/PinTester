import wiringpi2 as wp
import math
import numpy
from time import sleep

def rise(pin):
    wp.digitalwire(pin, 0)
    sleep(1)
    wp.digitalwire(pin, 1)

def lower(pin):
    wp.digitalwire(pin, 0)

#def auto():





solonoid = [7,11,13,15,18]
prompt1 = "which solonoids do you want to test? enter: a number between 1 and 8 "

wp.wiringPiSetupPhys()
wp.pinMode(solonoid[1], 1)
wp.pinMode(solonoid[2], 1)
wp.pinMode(solonoid[3], 1)
wp.pinMode(solonoid[4], 1)
wp.pinMode(solonoid[5], 1)




choice = raw_input("would you like to control the device manually or would you like it to be automatic, m = manual a = automatic")
# inset condition to turn all pins off after l0 seconds
if choice == "m":
    m  = True
    on = []
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
        for j in range(0,len(on)):
            rise(solonoid(on[j]))

elif choice == "a":
    print("working on it")


