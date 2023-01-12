import numpy as np
from scipy  import integrate
import math as m
import matplotlib.pyplot as plt
import matplotlib as cm
from math import sqrt

def Hws(ss,sg):
    Ks = 1.2
    ph= 20E3
    sigY = 235E6
    tws = 0.01
    
    y = 0.33*sqrt((Ks*ph*ss)/(sigY*tws))*sg
    return y

vHws= np.vectorize(Hws)
ss, sg = np.meshgrid(np.linspace(0.3,1.2,10), np.linspace(1,4,10))

HWS = vHws(ss,sg)

fig = plt.figure(figsize= (16,9))
ax = plt.axes(projection="3d")
surf = ax.plot_surface(ss,sg,HWS ,linewidth=0)
ax.set_xlabel("iets")
ax.set_ylabel("nogiets")
fig.colorbar(surf,shrink=0.5,aspect=5)
plt.show()
