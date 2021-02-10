# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:39:35 2021

@author: JOHN WARUTUMO
"""

import numpy as np
import matplotlib.pyplot as plt

'''
draw a picture from an array
'''
b=5;plt.imshow(np.arange(0,b**2).reshape(b,b))