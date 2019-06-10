import pandas as pd
import datetime
import  csv

from numba import cuda,vectorize

import cv2                                                                      # openCV
import numpy as np                                                              # for numpy arrays
import sqlite3
import os                                                                       # for creating folders


cap = cv2.VideoCapture(0)

                                                 
#  calling the sqlite3 database

Id = input("lecture no. :")
print(Id)
folderName = "lecture" + str(Id)                                                        # creating the person or user folder
folderPath =  "testing/"+folderName
if not os.path.exists(folderPath):
    os.makedirs(folderPath)


sampleNum = 0
sampleNum1 = 0
while(True):
    ret, img = cap.read()                                                       # reading the camera input

    

cap.release()                                                                   # turning the webcam off
cv2.destroyAllWindows()                                                         # Closing all the opened windows


#X = datetime.datetime.now().strftime ("%Y" + "/" + "%m" + "/" + "%d")
        
