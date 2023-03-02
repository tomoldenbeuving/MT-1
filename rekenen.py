import numpy as np
from scipy  import integrate
import math as m
import matplotlib.pyplot as plt
import matplotlib as cm
from math import sqrt

v_m = 1.59328
v_s = 13.5*0.51444
L_s = 31.5
L_m = 31.5/19
R_ts = 100.793*10**3
vis_s = 1.2873E-6
vis_m = 1.0811E-6
rho_s = 1026.6376
rho_m = 998.778
s_s = 272.6
s_m = 272.6/(19**2)

Re_s = (v_s*L_s)/vis_s
Re_m = (v_m*L_m)/vis_m

R_tm = 0.5*rho_m*v_m**2*s_m*(0.075/(m.log10(Re_m)-2)**2 + (2*R_ts)/(rho_s*v_s**2*s_s) - 0.075/(m.log10(Re_s)-2)**2)

print(R_tm)