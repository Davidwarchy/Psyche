# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 17:49:31 2021

@author: JOHN WARUTUMO
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

p = pd.read_csv("C:/Users/JOHN WARUTUMO/Desktop/daily-min-temperatures.txt")
l = pd.read_csv("liouville_summation_to_1e5.csv")

N = len(p)

def sconv(a,b):
    if len(b) > len(a):#make a have a greater length
        c = a
        a,b = b,c
        
    lena,lenb,lenab = len(a),len(b),len(a)+len(b)
    n = np.zeros((lenb,lenab-1))
    for x in range(lenb):
        B = b[:x+1]
        conv = np.convolve(a, B)
        n[x,:lena+len(B)-1] = conv
    return n

tml = []
for x in range(10):
    start = time.time()
    conv = sconv(np.array(p['Temp']), np.array(l)[:len(p)+10].flatten())
    end = time.time()
    tm = end-start
    tml.append(tm)
#fig,ax= plt.subplots(figsize=(16,8))
#ax.imshow(conv)
#plt.show()

#average_with_len
# Out[203]: 
# array([6.15622187, 6.27006149, 6.55649614, 5.97409511, 6.22022057,
#        6.26198888, 6.43740296, 6.32817221, 6.37499499, 5.93986106])
# array([6.15622187, 6.27006149, 6.55649614, 5.97409511, 6.22022057,
#        6.26198888, 6.43740296, 6.32817221, 6.37499499, 5.93986106])