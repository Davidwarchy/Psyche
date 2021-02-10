# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 09:10:56 2020

@author: JOHN WARUTUMO

computer program to draw the time-domain expression for a signal having the following profile in the frequency domain:
    1. all frequencies have equal magnitudes
    2. all frequencies have zero-phase shift - they aren't displace wrt the origin
"""

import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(-1*np.pi,np.pi,1001)#~12.5 allows 2 cycles as it is 4pi rads

#calculate values for series of different frequencies. Each array represents a sinusoid of a single frequency
s  = [np.cos(x*n) for x in range(0,2000)]

#add all functions vertically (in python, along the axis 0)
agg = np.sum(s,axis=0)

plt.stem(n,agg)

#peak won't show if the number of points is odd which is because n = 0 isn't reprented which is where the peak occurs.
#using the interval [0,2*pi] manifests 2 peaks at the boundaries.