# -*- coding: utf-8 -*-
"""

@author: Khilan

"""
import os
import cv2
import numpy as np
import pandas as pd

imgwithlabel=[]


#change below path according to your rock directory location

ppath=os.getcwd()+"\\rock"

for item in os.listdir(ppath):
    img=cv2.imread(os.path.join(ppath,item))

    #Before further processing verify image displaying or not
    #cv2.imshow("frame",img)
    #k=cv2.waitKey(20)
    #if k==27:
    #    break
    #dimensions = img.shape
    # height, width, number of channels in image
    #height = img.shape[0]
    #width = img.shape[1]
    #channels = img.shape[2]
    #print(str(height)+" "+str(width)+" "+str(channels))

    imgwithlabel.append([img,0])

cv2.destroyAllWindows()


#change below path according to your paper directory location
ppath=os.getcwd()+"\\paper"

for item in os.listdir(ppath):
    img=cv2.imread(os.path.join(ppath,item))

    #Before further processing verify image displaying or not
    #cv2.imshow("frame",img)
    #k=cv2.waitKey(20)
    #if k==27:
    #    break
    #dimensions = img.shape
    # height, width, number of channels in image
    #height = img.shape[0]
    #width = img.shape[1]
    #channels = img.shape[2]
    #print(str(height)+" "+str(width)+" "+str(channels))

    imgwithlabel.append([img,1])

cv2.destroyAllWindows()

#change below path according to your scissor directory location
ppath=os.getcwd()+"\\scissor"

for item in os.listdir(ppath):
    img=cv2.imread(os.path.join(ppath,item))

    #Before further processing verify image displaying or not
    #cv2.imshow("frame",img)
    #k=cv2.waitKey(20)
    #if k==27:
    #    break
    #dimensions = img.shape
    # height, width, number of channels in image
    #height = img.shape[0]
    #width = img.shape[1]
    #channels = img.shape[2]
    #print(str(height)+" "+str(width)+" "+str(channels))

    imgwithlabel.append([img,2])

cv2.destroyAllWindows()



#Now we have data of image with its label in imgwithlabel
#Without * error of too many value to unpack
imgdata,imglabel=zip(*imgwithlabel)

imglabel=np.array(imglabel)


copyimglabel=imglabel

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.compose import ColumnTransformer

ct = ColumnTransformer([("imglabel", OneHotEncoder(), [0])])
copyimglabel = copyimglabel.reshape(-1, 1)

copyimglabel = ct.fit_transform(copyimglabel)


from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

classify=Sequential()

classify.add(Convolution2D(32,3,3,input_shape=(330,250,3),activation='relu'))
classify.add(MaxPooling2D(pool_size=(2,2)))
classify.add(Flatten())

classify.add(Dense(output_dim=128,activation='relu'))
classify.add(Dense(output_dim=3,activation='softmax'))


classify.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
classify.fit(np.array(imgdata),np.array(copyimglabel),epochs=2)

#Save the model
savepath = os.getcwd() + "\\rps.tf"
classify.save(savepath)
