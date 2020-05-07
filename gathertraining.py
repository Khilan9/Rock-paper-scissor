# -*- coding: utf-8 -*-
"""

@author: Khilan

"""
import os
import cv2
camera=cv2.VideoCapture(0)
count=0
while True:
    _,frame=camera.read()
    cv2.rectangle(frame,(50,70),(300,400),(255,0,0),2)
    partfromframe=frame[70:400,50:300]

    #change below path according to your directory path and gather rock data
    #ex: ppath='E:/dataset/trainingdata/rock'
    #similary repeat for paper and scissor

    cv2.imwrite((os.path.join(ppath,'{name}{count}.jpg'.format(name="Rock",count=count))),partfromframe)
    count+=1
    if count==50:
        camera.release()
        break
    cv2.imshow('frame',frame)
    cv2.imshow('partframe',partfromframe)
    k=cv2.waitKey(1200)
    if k==27:
        camera.release()
        break

#Release the resources
camera.release()
cv2.destroyAllWindows()
