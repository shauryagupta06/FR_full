# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 02:54:18 2019

@author: piyush
"""

import cv2                                                                      # openCV
import numpy as np                                                              # for numpy arrays
import sqlite3
#import dlib
import os  
import csv                                                                     # for creating folders

cap = cv2.VideoCapture(0)
#detector = dlib.get_frontal_face_detector()

                                                               # closing the connection

name = input("Enter student's name : ")
roll = input("Enter student's Roll Number : ")
Id = input("id : ")

with open('mycsv.csv','a' , newline = '' ) as f:
    thewriter = csv.writer(f)
    thewriter.writerow([Id,roll,name])

#insertOrUpdate(Id, name, roll)                                                  # calling the sqlite3 database


folderName = "user" + str(Id)                                                        # creating the person or user folder
folderPath =  "train2_img/"+folderName
if not os.path.exists(folderPath):
    os.makedirs(folderPath)

sampleNum = 0
while(True):
    ret, img = cap.read()                                                       # reading the camera input
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                # Converting to GrayScale
#    dets = detector(img, 1)
    sampleNum += 1
    cv2.imwrite(folderPath + "/User." + Id + "." + str(sampleNum) + ".jpg",
                    img)                                                # Saving the faces
   #     cv2.rectangle(img, (d.left(), d.top())  ,(d.right(), d.bottom()),(0,255,0) ,2) # Forming the rectangle
    cv2.waitKey(200)                                                        # waiting time of 200 milisecond
    cv2.imshow('frame', img)                                                    # showing the video input from camera on window
    cv2.waitKey(1)
    if(sampleNum >= 50):                                                        # will take 20 faces
        break

cap.release()                                                                   # turning the webcam off
cv2.destroyAllWindows()                                                         # Closing all the opened windows
