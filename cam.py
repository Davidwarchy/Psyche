# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 13:43:01 2020

@author: David Warutumo
"""

import cv2
import time

cam =cv2.VideoCapture(0)
t = time.strftime('%Y%m%d%H%M%S',time.gmtime())

def camlad():
    cam =cv2.VideoCapture(0)
    ret, frame = cam.read()
    
    if not ret:
        print("error")
    else:
        cv2.imwrite('j.png',frame)
    cam.release()
    return frame

from PIL import Image
import numpy as np

x1 = camlad()
x2 = camlad()

def comp():
    xx = x1 - x2
    xx = np.dot(xx,[0.2989,0.5870,0.1140])
    imag = Image.fromarray(xx,'1')
    imag.show()