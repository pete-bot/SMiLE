## this one we are detecting edges using the wait for edge function 
## problem being that everythin needs to be done in a particular order to register the press

import RPi.GPIO as GPIO

#set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

#set up GPIO using BOARD numbering
#GPIO.setmode(GPIO.BOARD)


GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)



while True:
	GPIO.wait_for_edge(23, GPIO.RISING)
	print 'button 1 pressed'

	GPIO.wait_for_edge(23, GPIO.FALLING)
	print 'button 1 released'

	GPIO.wait_for_edge(24, GPIO.FALLING)
	print 'button 2 pressed'

	GPIO.wait_for_edge(24, GPIO.RISING)
	print 'button 2 released'


GPIO.cleanup()