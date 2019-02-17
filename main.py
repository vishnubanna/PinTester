import test
from os import popen
import manual_mode

choice = raw_input("would you like to use automatic or manual mode?")
while True:
    try:
        if choice == "a":
            test.automatic()
        elif choice == "m":
            manual_mode.main()
        else:
            choice = raw_input("would you like to use automatic or manual mode?")
    except KeyboardInterrupt:
        print("test ended")






