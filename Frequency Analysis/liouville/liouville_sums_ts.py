# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 04:55:51 2021

@author: JOHN WARUTUMO
"""

import math_functions
import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()
N = 1e4

n = np.arange(N)

#find the liouville of each number in N
sol = np.vectorize(math_functions.Liouville)
y = sol(n)
y = y.cumsum()

plt.grid(True)
plt.plot(n,y)

fig,ax = plt.subplots(figsize=(14,6))
ax.set_xscale('log')
ax.set_yscale('log')
ax.grid(True)
ax.plot(-y)

end_time = time.time()
taken_time = end_time - start_time
print("--- %s seconds ---" % (taken_time))