import autoMode
from os import popen
import manual_mode2


on = True
while on:
    choice = raw_input("would you like to use automatic or manual mode?")
    try:
        if choice == "a":
            autoMode.automatic()
        elif choice == "m":
            manual_mode2.main()
        else:
            choice = raw_input("would you like to use automatic or manual mode?")
    except KeyboardInterrupt:
        print("end")
        on = False
