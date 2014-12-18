#!/usr/bin/env python

# import our image manip-ulation tools
import numpy as np
import cv2

'''
# capture image from static. the 0 argument here changes the color spectrum:
# 1: color(no transperent), 0: greyscale, -1: unchanged (transperency preserved) 
img = cv2.imread('petrait.png', 0)

# primt the image in matrix form
#print img

# function that prints the image
cv2.imshow('peter-portrait', img) 

# wait for input
cv2.waitKey(0)

# close all windows after key is pressed
#cv2.destroyAllWindows()

# alternately, destroy specific window:
cv2.destroyWindow('peter-portrait')

# save the image
cv2.imwrite('peter-portrait.png', img)
'''

img = cv2.imread('petrait.png',0)
cv2.imshow('petrait', img)
userIn = cv2.waitKey(0) & 0xFF

# check for user input of esc
if userIn == 27:
	cv2.destroyAllWindows()
elif userIn == ord('s'):
	cv2.imwrite('peter-portrait.png',img)
	cv2.destroyAllWindows()