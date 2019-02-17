import wiringpi2 as wp
from pynput import keyboard
from pynput.keyboard import Key, Listener, KeyCode
import time

pk = keyboard
TIME_INIT = time.clock()
solonoid = [17,27,22,5,6]

wp.wiringPiSetupGpio()
wp.pinMode(solonoid[0], 1)
wp.pinMode(solonoid[1], 1)
wp.pinMode(solonoid[2], 1)
wp.pinMode(solonoid[3], 1)
wp.pinMode(solonoid[4], 1)

def manual():

    '''
    def PermLower(solonoid):
        on = True
        while(on):
            tim = 0
            tim = time.clock() - TIME_INIT
            if (time.clock() - TIME_INIT > 9):
                print("limit reached, all pins lowered")
                on = False
    '''

    def getChar(key):
        if (key, KeyCode):
            try:
                return key.char
            except:
                return str(key)

    def on_press(key):
        choice = getChar(key)
        try:
            choice = int(choice)
        except:
            print ("not a solonoid")
            choice = "invalid"
        for i in range(0,len(solonoid)):
            try:
                if solonoid[choice-1] == solonoid[i] :
                    print("solonoid {} is raised".format(getChar(key)))
                    wp.digitalWrite(solonoid[i], 1)
            except:
                print("non existents solonoid, only choice from 1 - 5 please")
        else:
            print("invalid: {}".format(choice))
        pass

    def on_release(key):
        choice = getChar(key)
        try:
            choice = int(choice)
        except:
            print ("not a solonoid")
            choice = "invalid"
        for i in range(0,len(solonoid)):
            try:
                if solonoid[choice-1] == solonoid[i]:
                    print(f"solonoid {getChar(key)} is raised")
                    wp.digitalWrite(solonoid[i], 0)
            except:

        if key == Key.esc:
            wp.digitalWrite(solonoid[0], 0)
            wp.digitalWrite(solonoid[1], 0)
            wp.digitalWrite(solonoid[2], 0)
            wp.digitalWrite(solonoid[3], 0)
            wp.digitalWrite(solonoid[4], 0)
            return False
        pass

    with Listener (on_press = on_press, on_release = on_release) as listener:
        listener.join()
