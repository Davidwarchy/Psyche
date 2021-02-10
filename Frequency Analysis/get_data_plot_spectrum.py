# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 12:25:27 2020

@author: JOHN WARUTUMO
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#since am dealing mostly with csvs, the script will specialize in that. later versions may look at what the user mostly inputs and bring up issues (like git) so that new types of files can be dealt with.
p = pd.read_csv("C:/Users/JOHN WARUTUMO/Desktop/daily-min-temperatures.txt")
colname = p.columns[1]#assuming that 1st column is the timestamp, 2nd the corresponding data value

n = np.array(p[colname])
n = np.mod((n*10),10)
N = n.size
ff = np.fft.fft(n-n.mean())
f = np.linspace(0,2*np.pi*365/(2*np.pi),N)

b=N//2
fig,ax = plt.subplots(1,1,figsize=(15,10))
ax.stem(f[:b],np.abs(ff)[:b])
#get the periods across which cycles end and begin

af = abs(ff)[:N//2]
cut = np.sort(af)[::-1][5]#get cut for top 5
ind = np.where(af>cut)#indices of top 5 largest frequencies
rf = f[ind]#values of frequncies in radians


def bokez():
    from bokeh.plotting import figure, output_file, show
    # prepare some data
    x = f
    y = np.abs(ff)
    
    # output to static HTML file
    output_file("lines.html")
    
    # create a new plot with a title and axis labels
    p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
    
    # add a line renderer with legend and line thickness
    p.line()(x, y, legend_label="Temp.", line_width=2)
    
    # show the results
    show(p)

