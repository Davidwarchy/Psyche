# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 12:53:25 2020

@author: JOHN WARUTUMO
"""
import cv2

class cam():
    def __init__(self):
        self.start()
        
    def start(self):
        self.v = cv2.VideoCapture(0)
    
    #what does the camera get from sorroundings
    def know(self):
        #capture frame
        ret, frame = self.v.read()
        return frame
                  
    def stop(self):
        self.v.release()
        
class mic():