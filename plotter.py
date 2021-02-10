# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 09:41:50 2020

@author: David Warutumo
"""
import pandas as pd
import numpy as np
import argparse

#command line options
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename',help='select file with timedata to plot ')
args = parser.parse_args()
fname = args.filename

f = open(fname,'r')
c = f.read()
f.close()

#separate lines into individual strings
c = c.split(sep="\n")

#create a list of pairs
y = [x.split(sep=':') for x in c] 
p = pd.DataFrame(y, columns=['time','value'])
p['time'] = pd.to_datetime(p['time'])
p['time'] = p['time'].map(lambda x:x.replace(second=0))
start = p.min()
end = p.max()
dates = pd.date_range(start=start[0],end=end[0],freq='1min')
p = p.set_index('time')
#drop duplicated values in index
p = p[~p.index.duplicated(keep='first')]
p = p.reindex(dates)

p = p.astype({'value':'float'})
p.plot()

def daily_values(p, date):
    d = pd.to_datetime(date)#d is the datetime object
    m = p.index.date == d
    return p[m]

#returns first n values of a specified date
def daily_part(p, date, first):
    d = pd.to_datetime(date)#d is the datetime object
    m = p.index.date == d
    return p[m][:first]

def plot_ma(p,v):
    d = pd.DataFrame(p)
    d = d.fillna(method='ffill')
    d['sma'] = d.iloc[:,0].rolling(window=v).mean()
    d.plot()

#returns dataframe with value against time, with days in each column
def comp_daily(p):
    d = pd.DataFrame()
    s,e = start[0].replace(hour=0,minute=0),end[0].replace(hour=0,minute=0)
    dates = pd.date_range(s,e,freq='1D')
    uniq = np.unique(dates.date)
    d = d.reindex( pd.date_range('20200909','20200910',freq='1Min',closed='left').time )
    for x in uniq:
        _ = daily_values(p,x)
        _.index = _.index.time
        d[str(x.strftime("%Y%m%d"))] = _
        
    return d
    
b = comp_daily(p)
b= b.fillna(method='ffill')
b = b.fillna(method='bfill')
#b['20200910'].plot().plot(b['20200909'])

import matplotlib.pyplot as plt
def freq_components(p):
    s = p[-int(5e4):].fillna(0)#eliminate nan values to make computation easier. concerned missing values may significantly affect analysis
    n = np.array(s).reshape((50000,))#flatten values to form a 1d signal
    n = n - n.mean()#get average to make dc value 0
    ff = np.fft.fft(n)
    N =  len(n)
    fx = np.linspace(0,2*np.pi/(60),N)
    plt.stem(fx[:N//2],abs(ff)[:N//2])
    #suprising this is that with even with missing data values the most dominant frequency is that which corresponds to one day (~86400s). 
    #also pleasantly surprised that the frequecies for 0.5, 0.25 of a day are next largest.
   #0.96 of a day period
   #I think I should publish my understanding of fourier transform - it is a representation of the amplitudes and phases of multifreq sinusoids. complex numbers are just a convenient way of representation, nothing more than that should be interpreted. 