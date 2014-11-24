## now we are going to use a hardware interrupt
## we poll for one switch and the other switch sets off a harware interrupt
## pretty smooth sailing biatches.

import RPi.GPIO as GPIO

#set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

#set up GPIO using BOARD numbering
#GPIO.setmode(GPIO.BOARD)


GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)


def printFunction(channel):
	print 'button 1 pressed'
	
	print 'notice how the bouncetime affects the button press'


GPIO.add_event_detect(23, GPIO.RISING, callback=printFunction, bouncetime=300)


while True:

	GPIO.wait_for_edge(24, GPIO.FALLING)
	print 'button 2 pressed'

	GPIO.wait_for_edge(24, GPIO.RISING)
	print 'button 2 released'


GPIO.cleanup()