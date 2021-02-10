# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 13:43:01 2020

@author: David Warutumo
"""

import cv2
import time

cam =cv2.VideoCapture(0)
t = time.strftime('%Y%m%d%H%M%S',time.gmtime())

def get_light_intensity():
    cam =cv2.VideoCapture(0)
    ret, frame = cam.read()
    
    if not ret:
        print("error")
    else:
        print("file")
        f = open('light_intensity_20210202.psy','a')
        f.write(time.strftime('%Y%m%d%H%M%S',time.gmtime())+':'+str(frame.mean())+'\n')
        f.close()
        
    cam.release()
    cv2.destroyAllWindows()
    
while True:
    get_light_intensity()
    time.sleep(60)