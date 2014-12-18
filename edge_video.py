#!/usr/bin/env python

# code to experiment with video - here we will capture, modify and record

# import our image manip-ulation tools
import numpy as np
import cv2
from matplotlib import pyplot as plt

# capture the video stream from camera (index 0 is default camera, 1 is 1st 2 is 2nd, etc)
capStream = cv2.VideoCapture(1)

# check input stream properties
#print capStream.get(3),
#print 'x',capStream.get(4)

# modify input stream resolution
capStream.set(3,640)
capStream.set(4,480)


# create a videowriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))


while(capStream.isOpened()):
    # capture frame by frame
    ret,frame = capStream.read()
    #ret, frame = capStream.read()
    if ret == True:
        # this flips every frame vertically
        frame = cv2.flip(frame,2)

    
        # our operations on the frame come here - convert image to grey (does not work anymore?)
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # display the resulting frames
     
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# release and close connections
capStream.release()
out.release()
cv2.destroyAllWindows()

