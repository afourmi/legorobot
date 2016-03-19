import RPIO
import time

RPIO.cleanup()
led = 3
sleep = 0.5

try:
	RPIO.setmode(RPIO.BOARD)
	RPIO.setup(led, RPIO.OUT, initial=RPIO.LOW)
	
	while True:
		RPIO.output(led, True)
		time.sleep(sleep)
		RPIO.output(led,False)
		time.sleep(sleep)

finally:
	RPIO.cleanup()

