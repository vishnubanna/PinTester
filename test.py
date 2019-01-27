import wiringpi2 as wp
from time import sleep

wp.wiringPiSetupGpio()
wp.pinMode(17, 1)
input = raw_input("run")
if input == "run":
  run = True
  while (run):
    try:
      wp.digitalwrite(17, 1)
      sleep(2)
      wp.digitalwrite(17, 0)
    except KeyboardInterrupt:
      run = False




