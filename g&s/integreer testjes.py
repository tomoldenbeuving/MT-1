import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
import math as m
x = np.array(np.arange(1000000))

def w(x,L):
    if x < L/6:
        q = (66/(5*L))*x
    elif x == L/6:
        q = -0.55
    elif L/6 < x < 5*L/6:
        q = -0.55
    elif x == 5*L/6:
        q = 2.2
    elif 5*L/6 < x < L :
        q = (-66/(5*L))*x + 13.2
    return q    

W = np.vectorize(w)
    
figure = plt.figure(figsize=[8,2])
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,W(x,1000000))
#plt.axhline(8,c="orange",label="minimale plaatdikte")
#plt.legend(loc = "lower right", shadow = True, fontsize="large")
plt.show()


def f(x,L):
    if x < L/6:
        q = (66/(10*L))*x**2
    elif L/6 <= x <= 5*L/6:
        q = -0.55*x + 11/60*L
    elif 5*L/6 < x < L :
        q = (-66/(10*L))*x**2 -11/60*L
    return q 

F = np.vectorize(f)

figure = plt.figure()
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,F(x,1000000))
#plt.axhline(8,c="orange",label="minimale plaatdikte")
#plt.legend(loc = "lower right", shadow = True, fontsize="large")
plt.show()
