import threading
from Que import Que
import time


q = Que()
threads = []
print_lock = threading.Lock()


def timer(tim,pin):
    global q
    q.lister()
    on = True
    while on:
        if (time.clock() - tim) > 8:
            with print_lock:
                print ("\n pin {} is off".format(pin))
                print (time.clock() - tim)
                on = False

def threader():
    on = True
    while on:
        global q
        pin = q.get()
        timeinit = time.clock()
        timer(timeinit, pin)
        on = q.tasks_done()

def control(pins):
    cont = raw_input("type a letter")
    if pins:
        print ("pin {} is on".format(cont))
        return cont
    else:
        print ("pin {} is on".format(cont))
        return False

if __name__ == "__main__":
    x = raw_input('Y/n')
    pins = True if (x == 'y') else False
    q.put(control(pins))
    while pins:
        pin = control(pins)
        if type(pin) == bool:
            pins == False
        q.put(pin)
        t = threading.Thread(target=timer, args=(time.clock(), q.get()))
        t.daemon = True
        t.start()
        #print("thread start")
        #print (threads)


