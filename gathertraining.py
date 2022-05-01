# -*- coding: utf-8 -*-
"""

@author: Khilan

"""
import os
import cv2
import sys 
import shutil
def main(argv):
    # Create Directory if not exist
    pathname = os.getcwd() + "\\" +  argv[1]
    isExist = os.path.exists(pathname)
    if not isExist:
        os.makedirs(pathname)
    else:
        shutil.rmtree(pathname, ignore_errors=True)
        os.makedirs(pathname)
    print(pathname)
    camera=cv2.VideoCapture(0)
    count=0
    while True:
        _,frame=camera.read()
        cv2.rectangle(frame,(50,70),(300,400),(255,0,0),2)
        partfromframe=frame[70:400,50:300]
        cv2.imwrite((os.path.join(pathname,'{name}{count}.jpg'.format(name=argv[1],count=count))),partfromframe)
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

if __name__ == "__main__":
    main(sys.argv)