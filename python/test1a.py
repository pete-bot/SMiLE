## this one we are just detecting high or low inputs
## problem: if button is down, it prints continuously

import RPi.GPIO as GPIO

#set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

#set up GPIO using BOARD numbering
#GPIO.setmode(GPIO.BOARD)


GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)



while True:
	if (GPIO.input(23) == 1):
		print 'button 1 pressed'
	
	if (GPIO.input(24) == 0):
		print 'button 2 pressed'

GPIO.cleanup()