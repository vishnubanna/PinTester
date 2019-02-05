import wiringpi2 as wiringpi
from time import sleep

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(17, 1)
wiringpi.pinMode(27, 1)
input = raw_input("run")
if input == "run":
  run = True
  wiringpi.digitalWrite(17, 0)
  wiringpi.digitalWrite(27, 0)
  while (run):
    try:
      wiringpi.digitalWrite(17, 1)
      sleep(1)
      wiringpi.digitalWrite(27, 1)
      print("HIGH")
      sleep(3)
      wiringpi.digitalWrite(17, 0)
      sleep(1)
      wiringpi.digitalWrite(27, 0)
      print("LOW")
      sleep(3)
    except KeyboardInterrupt:
      run = False
      wiringpi.digitalWrite(17, 0)
      wiringpi.digitalWrite(27, 0)
      sleep(1)
      print("end")



