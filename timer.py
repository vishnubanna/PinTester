import threading
from Que import Que
import time


q = Que()
threads = []
print_lock = threading.Lock()

def timer(tim,pin):
    global q
    on = True
    while on:
        if (time.clock() - tim) > 8:
            with print_lock:
                print ("\n pin {} is off".format(pin))
                print (time.clock() - tim)
                on = False

def control(pins):
    cont = input("type a letter")
    try:
        cont = int(cont)
    except:
        cont = cont
    if type(cont) == int:
        print ("pin {} is on".format(cont))
        q.put(cont)
        return cont
    else:
        return False

if __name__ == "__main__":
    x = input('y/n')
    pins = True if (x == 'y') else False
    if pins:
        try:
            test = []
            q.put(1)
            q.put(2)
            q.put(3)
            q.put(4)
            q.put(5)
            while q.has_values():
                q.lister()
                a = q.get()
                #rise(pin - 1, pin - 1)
                t1 = threading.Thread(target= timer, args=(time.clock(), a))
                t1.daemon = True
                t1.start()
                test.append(t1)
            for thread in test:
                thread.join()
        except:
            print("error")
    try:
        while pins:
            pin = control(pins)
            if type(pin) != bool:
                q.lister()
                t = threading.Thread(target=timer, args=(time.clock(), q.get()))
                t.daemon = True
                t.start()
                threads.append(t)
            else:
                print("ending")
                #print(threads)
                for thread in threads:
                    if thread.isAlive():
                        print(thread)
                        thread.join()
                q.put(1)
                q.put(2)
                q.put(3)
                while q.has_values():
                    print(q.has_values())
                    q.lister()
                    t = threading.Thread(target=timer, args=(time.clock(), q.get()))
                    t.start()
                    threads.append(t)
                print("done")
                for thread in threads:
                    thread.join()
                pins = False
    except KeyboardInterrupt:
        print("done")
