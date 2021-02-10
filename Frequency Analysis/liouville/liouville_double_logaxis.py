import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

p = pd.read_csv("C:/Users/JOHN WARUTUMO/Desktop/daily-min-temperatures.txt")
l = pd.read_csv("liouville_summation_to_1e5.csv")

fig,ax = plt.subplots(figsize=(18,10))
ax.grid(True)
ax.set_yscale('log')
ax.set_xscale('log')
ax.plot(np.log10(-l))
