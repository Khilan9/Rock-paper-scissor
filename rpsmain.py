# -*- coding: utf-8 -*-
"""

@author: Khilan

"""

import os
import cv2
import numpy as np
import pandas as pd
from keras.models import load_model

#location of file rps.tf
rpsmodelpath = os.getcwd() + "\\rps.tf"
classify=load_model(rpsmodelpath)

def findwinner(p1,p2):
    if p1==p2:
        return 0
    if p1==0:
        #p1 has paper
        if p2==1:
            #p2 has Rock
            return 1
        elif p2==2:
            #p2 has Scissor
            return -1
    elif p1==1:
        #p1 has Rock
        if p2==0:
            #p2 has Paper
            return -1
        elif p2==2:
            #p2 has Scissor
            return 1
    elif p1==2:
        #p1 has Scissor
        if p2==0:
            #p2 has Paper
            return 1
        elif p2==1:
            #p2 has Rock
            return -1
    return 0

cap=cv2.VideoCapture(0)
cv2.namedWindow("Play window",cv2.WINDOW_NORMAL)
while True:
    _,frame=cap.read()

    #Draw the rectangles and take region of interest of player1 and player2
    cv2.rectangle(frame,(50,70),(300,400),(0,0,255),2)

    cv2.rectangle(frame,(330,70),(580,400),(255,0,0),2)
    player1frame=frame[70:400,50:300]
    player2frame=frame[70:400,330:580]

    #dimensions = player1frame.shape

    #height = player1frame.shape[0]
    #width = player1frame.shape[1]
    #channels = player1frame.shape[2]
    #print(str(height)+" "+str(width)+" "+str(channels))


    #Predict the move of player
    player1pred=classify.predict(np.array([player1frame]))
    player2pred=classify.predict(np.array([player2frame]))
    v1=np.max(player1pred)
    v2=np.max(player2pred)
    p1=np.where(player1pred==v1)
    p2=np.where(player2pred==v2)
    print(player1pred)
    print(player2pred)
    print(p1[1][0])
    print(p2[1][0])
    print(findwinner(p1[1][0],p2[1][0]))
    print("-------------------------------------------------------------------")

    if findwinner(p1[1][0],p2[1][0])==1:
        #Player1 is winner
        cv2.putText(frame,"Winner",(50,70),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
    elif findwinner(p1[1][0],p2[1][0])==-1:
        #Player2 is winner
        cv2.putText(frame,"Winner",(330,70),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
    elif findwinner(p1[1][0],p2[1][0])==0:
        #Tie
        cv2.putText(frame,"Tie",(190,70),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),3)


    cv2.imshow("Play window",frame)

    k=cv2.waitKey(1)
    if k==27:
        break

#Release the resources
cap.release()
cv2.destroyAllWindows()
