# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 08:17:38 2021

@author: JOHN WARUTUMO

Program that desires to model the stream of relationship between time series values and a time-frequency or correlation tool.
"""
import math_functions
import pandas as pd
import numpy as np

def secsToString(s):
    return str(int(s))+'s'

def liouvilleSum(n):
    N = n
    n = np.arange(N)
    #find the liouville of each number in N
    sol = np.vectorize(math_functions.Liouville)
    y = sol(n)
    return y.cumsum()

p = pd.read_csv("C:/Users/JOHN WARUTUMO/Desktop/usdchf.csv")
p.columns = p.columns.str.lower()#make columns lowercase
"""
If the values follow a time series, detect the period of the time series
"""
time_marker = 'date'
td = pd.to_datetime(p[time_marker])#convert date or time column to datetime object
p.index = td#to allow p to be joined to a more complete index of time
td = td.diff(1)#subtract next from current row
md = td.median()#find the probable time difference
md = md.total_seconds()
"""
Index the data to the period
"""
start = p[time_marker][0]
start = pd.to_datetime(start)
end = p[time_marker].iloc[-1]
end = pd.to_datetime(end)
dates = pd.date_range(start=start,end=end,freq=secsToString(md))#create time axis
d = pd.DataFrame(data=p,index=dates)
d = d.drop(columns=['date'])
"""
generate the function to convolve with 
"""
g = liouvilleSum(10000)
"""
describe the dimensions being explored
"""
dim0 = np.arange(len(d))#length of data in its highest resolution (native form, some may say - google in particular)
dim1 = np.array(d[d.columns[1]])
dim2 = 