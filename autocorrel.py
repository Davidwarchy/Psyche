# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:32:00 2020

@author: JOHN WARUTUMO
"""
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf, acf

s = pd.read_csv("C:/Users/JOHN WARUTUMO/Desktop/daily-min-temperatures.txt",header=0,index_col=0)

plot_acf(s,lags=365)