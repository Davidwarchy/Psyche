# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 05:51:52 2021

@author: JOHN WARUTUMO
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

p = pd.read_csv("C:/Users/JOHN WARUTUMO/Desktop/mpesa.csv")
colname = p.columns[1]#assuming that 1st column is the timestamp, 2nd the corresponding data value
n = np.array(p[colname])

N = n.size

ff = np.fft.fft(n-n.mean())
f = np.linspace(0,(2*np.pi),N)

b=N//2
plt.stem(f[:b],np.abs(ff)[:b])
#get the periods across which cycles end and begin

af = abs(ff)[:N//2]
cut = np.sort(af)[::-1][5]#get cut for top 5
ind = np.where(af>cut)#indices of top 5 largest frequencies
rf = f[ind]#values of frequncies in radians
frq = rf/(2*np.pi)
T = 1/frq
harms = T[0]*frq
pdt = pd.to_datetime(p[p.columns[0]])
dlt = pdt[1] - pdt[0]
scs = dlt.total_seconds()

#suicide 6 month cycle is strongest
#superbowl yearly cycle is strongest -- people talk more about superbowl in 1 year cycles than in greater or lesser cycles
#penis 6 month cycle is strong
#mpesa has 8 month cycle that is strong and weaker 1 month cycles.