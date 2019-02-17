import time
import threading
import wiringpi2 as wp
from Que import Que

TIME_INIT = time.clock()
q = Que()
pin_lock = threading.Lock()
solonoid = [17,27,22,5,6]
resis = [20,24,12,16,20]
rised = [0]*len(solonoid)
threads = []

# controll the rasing and lowering of the pins with an actual button make 5 pins input pins( and read the input) as long as input is on or voltage is on the pins will be raised

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


def manual():
    try:
        global rised
        count = 0
        pin = raw_input("which pin raised or lowered?")
        if pin == 'a':
            print("exiting")
            return False
        pin = int(pin)
        if (pin >= 1 and pin <= 5):
            if rised[pin-1] == pin:
                count -= 1
                lower(pin-1, pin-1)
                rised[pin-1] = 0
                print(rised)
                print("pin {} lowered".format(pin))
                return "lowered"
            elif rised[pin-1] == 0:
                rise(pin-1, pin-1)
                q.put(pin)
                count += 1
                rised[pin-1] = pin
                print(rised)
                print("pin {} has been raised".format(pin))
                return "rised"

        else:
            pass
    except KeyboardInterrupt:
        print("manual off")
        return False

def rise(sol, res):
    global TIME_INIT
    wp.digitalWrite(solonoid[sol], 0)
    time.sleep(0.00001)
    wp.digitalWrite(resis[res], 1)
    time.sleep(0.00001)
    TIME_INIT = time.clock()
    wp.digitalWrite(solonoid[sol], 1)
    time.sleep(0.00002)
    wp.digitalWrite(resis[res], 0)
    return

def lower(sol, res):
    wp.digitalWrite(solonoid[sol], 1)
    time.sleep(0.00002)
    wp.digitalWrite(resis[res], 0)
    time.sleep(0.00002)
    wp.digitalWrite(solonoid[sol], 0)
    time.sleep(0.002)
    wp.digitalWrite(resis[res], 1)
    return

def timer(tim,pin):
    global q
    global rise
    on = True
    while on:
        global solonoid, resis
        if (time.clock() - tim) > 5:
            #with pin_lock:
                wp.digitalWrite(solonoid[pin - 1], 0)
                time.sleep(0.00002)
                wp.digitalWrite(resis[pin - 1], 1)
                print ("\n pin {} is off".format(pin))
                print (time.clock() - tim)
                on = False 
                #rise[pin-1] = 0

def main():
    on = True
    print("maunual mode - initial start up test")
    if on:
        try:
            test = []
            q.put(1)
            q.put(2)
            q.put(3)
            q.put(4)
            q.put(5)
            rise(0,0)
            rise(1,1)
            rise(2,2)
            rise(3,3)
            rise(4,4)
            while q.has_values():
                q.lister()
                pin = q.get()
                t1 = threading.Thread(target= timer, args=(time.clock(), pin))
                t1.daemon = True
                t1.start()
                test.append(t1)
            for thread in test:
                thread.join()
        except:
            print("error")
    try:
        while on:
            valid = manual()
            if valid == "rised":
                t = threading.Thread(target= timer, args=(TIME_INIT, q.get()))
                t.daemon = True
                t.start()
                threads.append(t)
            elif valid == "lowered":
                print("pin lowered")
            elif valid == False:
                print("ending")
                for thread in threads:
                    if thread.isAlive():
                        print(thread)
                        thread.join()
                on = False
                return
            else:
                print("all pins raised")
    except KeyboardInterrupt:
        on = False
        return
