#!/usr/bin/env python

# code to experiment with video - here we will capture, modify and record

# import our image manip-ulation tools
import numpy as np
import cv2

# capture the video stream from camera (index 0 is default camera, 1 is 1st 2 is 2nd, etc)
capStream = cv2.VideoCapture(0)

# check input stream properties
#print capStream.get(3),
#print 'x',capStream.get(4)

# modify input stream resolution
width = 1920
height = 1080
fps = 20.0

# create a videowriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('out.avi',fourcc, fps,(width,height))


while(capStream.isOpened()):
    # capture frame by frame
    ret,frame = capStream.read()
    #ret, frame = capStream.read()
    if ret == True:
        
        #print frame;
        #img = cv2.imread('messi5.jpg',0)
        #cvtColor(frame, edges, COLOR_BGR2GRAY)
        #GaussianBlur(edges, edges, Size(7,7))
        edges = cv2.Canny(frame,100,200)

        # print edges;
        #plt.subplot(121),plt.imshow(frame,cmap = 'gray')
        #plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        #plt.subplot(122),plt.imshow(edges,cmap = 'gray')
        #plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

        #plt.show()

        #out.write(edges)

        cv2.imshow('edges',edges)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# release and close connections
capStream.release()
out.release()
cv2.destroyAllWindows()


'''

# modify input stream resolution
width = 640
height = 480
fps = 24.0

# create a videowriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter('out.avi',fourcc, fps,(width,height))


while(capStream.isOpened()):
    # capture frame by frame
    ret,frame = cap.read()
    #ret, frame = capStream.read()
    if ret == True:

        cv2.VideoCapture.grab(cap)
        ret2, frame = cv2.VideoCapture.retrieve(cap)
        cv2.WriteFrame(writer,frame)        

        #img = cv2.imread('messi5.jpg',0)
        #cv2.cvtColor(frame, frame, COLOR_BGR2GRAY)
        #GaussianBlur(edges, edges, Size(7,7))
        #edges = cv2.Canny(frame,100,200)




        #out.write(edges)

        cv2.imshow('canny output',edges)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# release and close connections
capStream.release()
out.release()
cv2.destroyAllWindows()

'''
