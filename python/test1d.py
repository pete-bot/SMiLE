## Now I am going to play around a bit, try and make it a bit more functional.
## Worth noting that you can't have two detection events for the one GPIO
## even if they are different edges we are detecting.

## it looks like we are only allowed to have one detection event per GPIO
## i.e. can't have two different hardware interrupts for the one pin 
##	(even if one is rising and the other is falling)
## Also cannot have a hardware interrupt if the GPIO is being detected elsewhere in code
## But we can detect it in code as much as we like because of it's linear structure.

import RPi.GPIO as GPIO

#set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

#set up GPIO using BOARD numbering
#GPIO.setmode(GPIO.BOARD)


GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)


def printFunction(channel):
	if (GPIO.input(23) == True):
		print 'button 1 pressed'
	else:
		print 'button 1 released'


def printFunction2(channel):
	if (GPIO.input(24) == True):
		print 'button 2 released'
	else:
		print 'button 2 pressed'


#the button I'm using for this has a bounce time of ~10ms (the little black button)
#It's pretty tough to get an error out of it when using 15
GPIO.add_event_detect(23, GPIO.BOTH, callback=printFunction, bouncetime=15)

#Using the same time for the larger button even though I couldn't find the datasheet
GPIO.add_event_detect(24, GPIO.BOTH, callback=printFunction2, bouncetime=10)



while True:
	pass


GPIO.cleanup()