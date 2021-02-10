# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 18:51:20 2020

@author: JOHN WARUTUMO
"""

import numpy as np
import matplotlib.pyplot as plt

#def compTransformation(arr):
#arr = np.array([1,0,0,1,0,1,1,0,0,3,0,0,4,0,0,1])
x = np.linspace(0,4*np.pi,1001)
y1,y2,y3 = np.cos(10*x),np.cos(20*x),np.cos(3*x)
arr = y1+y2+y3
farray = np.fft.fft(arr)
ifarray = np.fft.ifft(farray)
#compare original and inverse fourier transform to see how operation changes values
#original and inverse transform are equals except at spots where values were approximately 0.
c = np.corrcoef(arr,ifarray.real)#correlation coefficient matrix for both matrices
c = abs(c[0][1])
    # if c > 0.95:
    #     return True
    # else:
    #     return False

if c == 1.0:
    print("fourier processing preserves original signal")
else:
    print("processing doesn't preserve signal")

#plotting
f_ax = np.linspace(0,2*np.pi/(4*np.pi/1e3),1001)
plt.xlabel('f')
plt.ylabel('X[f]')
plt.xlim(0,30)#show only frequencies upto 30Hz for better visual
plt.stem(f_ax,farray)

#right now the question I wish to answer is: what is the relationship between the sampling period in the t-domain and the values in the x-axis of the frequency domain. when a dft is performed what also is the relationship between the sampling periods in the t-domain and the f-domain. 202012271022: If the sampling period is ts, then the largest frequency that can b represented is 1/ts. The FT function is periodical with omega, w = 2*pi. All frequencies in the signal are accomodated within any interval of 2*pi. For the interval [0,2*pi] the maximum frequency is 2*pi/ts, the frequency corresponding to the sampling period of the signal. 

#combination of inputs equals combination of individual transformations - iow (in other words), fourier transform of a series can be represented as the sum of the fourier transform of single events
#working on a single event at n = 0 (known in books as the unit-sample, because it's only one event and has mag of 1) and playing about with it reveals some awesome observations including:
        #at n = 0 and x[n] = 1, the fourier transform X(f) = 1 and isn't complex. this means that all frequencies are of equal magnitude and don't have a phase shift from the origin.
        #if the event is moved to n = 2, X(f) = e**(-jw*2) which can be translated as a fucntion of frequencies all having a magnitude of 1, but having phase shifts dependent on the frequencies. Magnitude = 1, Phase = -2w (omega). 
        