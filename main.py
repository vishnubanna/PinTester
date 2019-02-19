import test
from os import popen
import manual_mode2

choice = raw_input("would you like to use automatic or manual mode?")
while True:
    try:
        if choice == "a":
            test.automatic()
        elif choice == "m":
            manual_mode2.main()
        else:
            choice = raw_input("would you like to use automatic or manual mode?")
    except KeyboardInterrupt:
        print("test ended")






