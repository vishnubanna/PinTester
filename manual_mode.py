

import time
import threading
#import wiringpi2 as wp
import wp
from Que import Que

TIME_INIT = time.clock()
count = 0
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
        global count
        pin = raw_input("which pin raised or lowered?")
        try:
            pin = int(pin)
        except:
            pin = raw_input("which pin raised or lowered?")
        if (count <= 5) and (pin >= 1 and pin <= 5):
            if rised[pin-1] == pin:
                c -= 1
                lower(pin-1, pin-1)
                rised[pin-1] = 0
                print(rised)
                print("pin {} lowered".format(pin))
                return "lowered"
            elif rised[pin-1] == 0:
                rise(pin-1, pin-1)
                count += 1
                rised[pin-1] = pin
                print(rised)
                print("pin {} has been raised".format(pin))
                return pin
        elif count > 5:
            pass
        elif pin > 5:
            print("not a pin")
            pass
        elif pin == 0:
            return False
    except:
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
    time.sleep(0.00002)
    wp.digitalWrite(resis[res], 1)
    return

def timer(tim, pin, length):
    global q
    global rise
    on = True
    time.sleep(length)
    if (time.clock() - tim) > length:
            if rised[pin-1] == pin:
                with pin_lock:
                    lower(pin-1, pin-1)
                print(time.clock() - tim)
                print("time force pin {} lowered".format(pin))

def main():  on = True
    print("maunual mode - initial start up test")
    global rised
    if on:
        try:
            test = []
            q.put(1)
            q.put(2)
            q.put(3)
            q.put(4)
            q.put(5)
            q.lister()
            time.sleep(1)
            while q.has_values():
                q.lister()
                pin = q.get()
                rise(pin - 1, pin - 1)
                t1 = threading.Thread(target= timer, args=(time.clock(), pin, 1))
                t1.daemon = True
                t1.start()
                test.append(t1)
            for thread in test:
                thread.join()
            rised = [0]*len(solonoid)
        except:
            print("error")
    try:
        while on:
            valid = manual()
            if type(valid) == int:
                q.put(valid)
                q.lister()
                t = threading.Thread(target= timer, args=(TIME_INIT, q.get(), 5))
                t.daemon = True
                t.start()
                threads.append(t)
            elif valid == "lowered":
                print("pin lowered")
            elif valid == False:
                on = False
            else:
                print("all pins raised")
        print("ending")
        for thread in threads:
            if thread.isAlive():
                print(thread)
                thread.join()
    except KeyboardInterrupt:
        on = False


if __name__ == "__main__":
    main()

