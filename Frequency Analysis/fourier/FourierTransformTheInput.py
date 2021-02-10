# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 09:42:16 2021

@author: JOHN WARUTUMO
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#since am dealing mostly with csvs, the script will specialize in that. later versions may look at what the user mostly inputs and bring up issues (like git) so that new types of files can be dealt with.
def noOfCols(p):
    return len(p.columns)

#with assumption that a ts follows  chronology
def isDateCol(c):
    diff = pd.to_datetime(c).diff()
    gtlt = diff[1:] > pd.Timedelta(1, unit='ns')
    if gtlt.all():
        return True

def getFile(f):
    return pd.read_csv(f)
      
#calculate for fourier tranform of a single series or multiple series
def calcFft(n):
    if len(n.shape) == 1:
        N = n.shape[0]
        return abs(np.fft.fft(n - n.mean())[:N//2])
    else:
        N = n.shape[1]
        af = np.zeros(shape=(n.shape[0], n.shape[1]+1));
        i = 0
        for x in n:
            f = abs(np.fft.fft(x - x.mean())[:N//2])
            af[0] = f
            i+=1
        return af

#plot & show column names for single or multiple series
def plotFft(n, colNames, T=1):
    if len(n.shape) == 1:
        N = len(n)
        f = np.linspace(0,1/T,N)
        fig,ax = plt.subplots(figsize=(15,10))
        ax.grid(True)
        ax.set_title(colNames[0])
        ax.set_ylabel('Magnitude')
        ax.set_xlabel('Frequency')
        
        ind0 = dominantHeights(n,5)#indices of top N heights
        ind1 = np.setdiff1d(np.arange(N),ind0)
        ax.stem(f[ind0],n[ind0],'ro')
        ax.stem(f[ind1],n[ind1],'y*')
        plt.show()
        
    else:
        N = n.shape[1]
        f = np.linspace(0,1/T,N)
        fig,axs = plt.subplots(len(n), figsize=(15,10))
        
        for ax,y,coln in zip(axs,n,colNames):
            ind0 = dominantHeights(y,5)#indices of top N heights
            ind1 = np.setdiff1d(np.arange(N),ind0)
            ax.stem(f[ind0],y[ind0],'ro')
            ax.stem(f[ind1],y[ind1],'y*')
            ax.title(coln)
            ax.grid(True)
        plt.show()

#get top N values in an array y            
def dominantHeights(y,N):
   cut = np.sort(y)[::-1][N]#get cut for top 5
   return np.where(y>cut)#indices of top 5 largest frequencies

def getColumns(p):
    if(noOfCols(p) == 1):
        if(p.columns[0] != 0):
            return p.columns[0]
        else:
            return 'series 1'
    else:
        if(p.columns[0] != 0):
            return p.columns
        else:
            return ['series '+str(x+1) for  x in range(len(p.columns))]

def getTimedelta(p):
    c = pd.to_datetime(p)
    diff = c.diff()#get the difference between consecutive days
    if abs( (diff.mean() - diff.max())/diff.max()*100 ) < 50:
        delta = diff.median().total_seconds()
        return delta
   #else:show error

        
def main(fname):
    p = getFile(fname)#if file is empty display alert
    tDelta = 1#1second for default
 
    if(noOfCols(p) == 1):
        #perform fft and display
        cols = getColumns(p)
        f = calcFft(np.array(p))
        plotFft(f, cols)
    elif noOfCols(p) ==2:#first might be date
        if isDateCol(p[p.columns[0]]):
            tDelta = getTimedelta(p[p.columns[0]])
            #perform fft and display with indicated s.period
            cols = getColumns(p)
            f = calcFft(np.array(p[p.columns[1]]))
            plotFft(f,cols[1:],tDelta)#disregard time column
        else:
            #process multiple data columns
            cols = getColumns(p)
            f = calcFft( np.array(p) )
            plotFft(f, cols)
    else:
        if isDateCol(p[p.columns[0]]):
            tDelta = getTimedelta(p[p.columns[0]])
            ##process multiple data columns
            cols = getColumns(p)
            f = calcFft(np.array(p[p.columns[1]]))
            plotFft(f,cols[1:],tDelta)#disregard time column
        else:
            ##process multiple data columns
            cols = getColumns(p)
            f = calcFft( np.array(p) )
            plotFft(f, cols)
            
main("C:/Users/JOHN WARUTUMO/Desktop/daily-min-temperatures.txt")


