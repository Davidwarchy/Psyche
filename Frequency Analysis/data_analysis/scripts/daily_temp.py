# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 16:06:47 2020

@author: JOHN WARUTUMO
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

p = pd.read_csv("C:/Users/JOHN WARUTUMO/Desktop/daily-min-temperatures.txt")
colname = "Temp"

n = np.array(p[colname])
num = n.size

#sampling period dt = 1, highest frequency = 2*pi/dt, sampling period of frequencies df = (2*pi/dt)/divisions

ff = np.fft.fft(n-n.mean())
f = np.linspace(0,(2*np.pi),num)

plt.xlim(0, 0.02)
plt.stem(f,ff)

#mystery to resolve.
#it's kind of obvious that temperature data is seasonal with (in) the year.
#Doing the fourier transform of the data shows that the greatest magnitudes are the dc values, followed by the the frequency that repeats once every 58 days. NB: 1Hz is measured as one cycle a day 20201228549: I have assumed a suggestion from the internet that the whole extent of the fourier transform is 2*pi/dt, where dt is the sampling period. so it might be reasoned that performing a fourier transform gives the amplitudes of various frequencies (interpreted as radian/day). Also a radian per day would be less than a whole cycle in that day. Since our sampling period is one day, the highest radian frequency is 2*pi/1day, which seems logical as we can't measure higher frequencies than the sampling frequency. To interpret the radian frequencies to days, we may get the radian frequency of interest and get its value in cycles per day by dividing it by 2*pi. That will be the coverage of the cycle done in a day. eg. 0.5 cycles per day may mean that half a cycle is covered each day. Whatever value we get is the fraction of the cycle of the corresponding frequency covered each day. 
    #for example if we select the radian frequency 0.017218923834419256
    #the matching frequency in cycles per day is 0.017218923834419256/2*np.pi = 0.002740476842970677. So in a day 0.027 of the cycle of this frequency is covered.
    #0.002740476842970677 per day will be fully covered in 1/0.002740476842970677 = 364.9 days. this matches our intuition. This method of reasoning seems rather forceful than deductive. I think there are a few things to be checked when using this method:
        #taking note of the sampling period - if its in days, the frequencies will be in rad/day; if in seconds, the frequency axis will read in radians per seconds. 
        #the maximum frequency in radians is 2*pi/ts, where ts is the sampling period.
        #to convert a frequency from radians to cycles, divide by 2*pi
        #to get the period of a cycle, invert the number of cycles per unit of measure (seconds, days, cm, etc...)
    
#why 58 when nothing in the data points to it? 20201228549: Question answered above in a way.