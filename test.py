import wiringpi2 as wiringpi
from time import sleep

def automatic():
  wiringpi.wiringPiSetupGpio()
  wiringpi.pinMode(17, 1)
  wiringpi.pinMode(27, 1)
  wiringpi.pinMode(22, 1)
  wiringpi.pinMode(5, 1)
  wiringpi.pinMode(6, 1)
  input = raw_input("run y/n")  

  if input == "y":
    run = True
    wiringpi.digitalWrite(17, 0)
    wiringpi.digitalWrite(27, 0)
    wiringpi.digitalWrite(22, 0)
    wiringpi.digitalWrite(5, 0)
    wiringpi.digitalWrite(6, 0)
    while (run):
      try:
        wiringpi.digitalWrite(17, 1)
        sleep(0.002)
        wiringpi.digitalWrite(27, 1)
        sleep(0.002)
        wiringpi.digitalWrite(22, 1)
        sleep(0.002)
        wiringpi.digitalWrite(5, 1)
        sleep(0.002)
        wiringpi.digitalWrite(6, 1)
        print("HIGH")
        sleep(0.2)
        wiringpi.digitalWrite(17, 0)
        sleep(0.002)
        wiringpi.digitalWrite(27, 0)
        sleep(0.002)
        wiringpi.digitalWrite(22, 0)
        sleep(0.002)
        wiringpi.digitalWrite(5, 0)
        sleep(0.002)
        wiringpi.digitalWrite(6, 0)
        print("LOW")
        sleep(0.2)
      except KeyboardInterrupt:  
        run = False
        wiringpi.digitalWrite(17, 0)
        wiringpi.digitalWrite(27, 0)
        wiringpi.digitalWrite(22, 0)
        wiringpi.digitalWrite(5, 0)
        wiringpi.digitalWrite(6, 0)
        sleep(1)
        print("end")



