# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 12:21:38 2021

@author: JOHN WARUTUMO
"""
import numpy as np
import matplotlib.pyplot as plt
#distance from the sun in km
au = 149,597,871
perihelion = 147098070#0.98329au
aphelion = 152097700#1.01671au

ph = 0.98329
ah = 1.01671

#equation of the ellipse is (y**2/a**2) + (x**2/b**2) = 1 where a = aphelion and p = perihelion.
#in polar coordinates with the sun focus at the origin, the formula is 
#r = (b**2/a)/(a- (c/a)*cos(theta)) where c**2 = a**2 - b**2
a,b  = ah,ph
c = np.sqrt(a**2-b**2)

theta = np.linspace(0,2*np.pi,365*10)
r = (b**2/a)/(a- (c)*np.cos(theta))
fig,ax = plt.subplots(figsize=(10,10), subplot_kw={'projection': 'polar'})
ax.plot(theta,r)
plt.show()