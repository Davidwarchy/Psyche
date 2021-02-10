# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 10:33:26 2021

@author: JOHN WARUTUMO
"""

import numpy as np
import matplotlib.pyplot as plt

n = np.arange(1,10)#x axis
y1 = n#straight line
y2 = n**2#power line
y3 = np.log(n)#log line

def layout(xy,labels):
    N = len(xy)
    fig,axs = plt.subplots(N,1,figsize=(15,9))
    i = 0
    for x in range(N):
        axs[i].stem(xy[i][0],xy[i][1])
        print("############################### "+(labels[i])+" ##############################")
        print("mean    :"+str(np.mean(xy[i][1])))
        print("median  :"+str(np.median(xy[i][1])))
        i += 1

layout( ((n,y1),(n,y2),(n,y3)), ['Linear','Power','Log'])
"""
bias may be calculated by finding the difference between mean and median, then comparing that the dynamic range of the data.The dynamic range is the maximum minus the minimu
"""
def bias(n):
    dr = np.max(n) - np.min(n)
    med = np.median(n)
    mean = np.mean(n)
    return (mean - med)/dr
'''
the bias can be stated to be the relative placement of the mean in the dynamic range wrt the median. Positive bias values place it on top while negative bias values place it below the median. The extent from the median is determined by the actual value of the bias. Linear distribution has the fairest amount of bias. Logarithmic distrition has negative bias - since 
'''
