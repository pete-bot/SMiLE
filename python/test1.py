## Now I am going to try to play with output.
##style edit, name all my pins to make sense

#GPIO.LOW == False == 0
#GPIO.HIGH == True == 1

import RPi.GPIO as GPIO

# toggles only on rising edge         RIGHT BUTTON
def buttonPress1(channel):
	if (ledToggle == False):
		ledToggle = True
	else:
		ledToggle = False

	GPIO.output(ledout, ledToggle)
	

#this input has a pull up resistor.
#toggles on rising and falling edge    LEFT BUTTON
def buttonPress2(channel):
	if (GPIO.input(button2) == False):
		ledToggle = True 
	else:	
		ledToggle = False
	GPIO.output(ledout, ledToggle)






while True:
	pass


GPIO.cleanup()




#def buttonPress2(channel):
#	if (GPIO.input(button2) == False):
#		GPIO.output(ledout, True) 
#	else:	
#		GPIO.output(ledout, False)




GPIO.add_event_detect(button1, GPIO.RISING, callback=buttonPress1, bouncetime=300)


GPIO.add_event_detect(button2, GPIO.BOTH, callback=buttonPress2, bouncetime=30)





# name our buttons, numbers correspond to gpio number not pin numbers
button1 = 23
button2 = 24
ledout = 18

#initialise variables
ledToggle = True


GPIO.setmode(GPIO.BCM)


GPIO.setup(button1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.setup(button2, GPIO.IN, pull_up_down = GPIO.PUD_UP)

GPIO.setup(ledout, GPIO.OUT)

