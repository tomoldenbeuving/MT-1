import numpy as np
from scipy  import integrate
import math as m
import matplotlib.pyplot as plt
import matplotlib as cm
from math import sqrt

np.errstate(divide = 'ignore') 
#v_m = 1.59328
v_m = np.arange(0,1.2,0.1)
v_m = np.delete(v_m,1)
R_tm = np.array([0.0,0.098,0.2,0.34,0.57,0.83,1.13,1.51,1.98,2.59,3.4])

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
g = 9.81

Re_s = (v_s*L_s)/vis_s
Re_m = (v_m*L_m)/vis_m

#R_tm = 0.5*rho_m*v_m**2*s_m*(0.075/(m.log10(Re_m)-2)**2 + (2*R_ts)/(rho_s*v_s**2*s_s) - 0.075/(m.log10(Re_s)-2)**2)

Fr = v_m/m.sqrt(g*L_m) 
Re = (v_m*L_m)/vis_m
C_fm = 0.075/(np.log10(Re)-2)**2
C_tm = (R_tm)/(0.5*rho_m*(v_m**2)*s_m)
frac1 = Fr**4/C_fm
frac2 = C_tm/C_fm



label = np.array(["V_m[m/s]","R_tm[N]","Fr[-]","Re[-]","C_fm[-]","C_tm[-]","Fr^4/C_fm[-]","C_tm/C_fm[-]"])

table = np.array([Fr,Re,C_fm,C_tm,frac1,frac2])

table_trans = table.T
def display():
        with np.printoptions(precision=3, suppress=True):
                print(table_trans)

rc = (1.33-1.28)/(0.2-0.1)
lin = np.arange(0.0,0.21,0.01)
k = 1.326-0.1
func = lin*rc+k

def plot():
        figure = plt.figure(figsize=(16,9))
        plt.xlabel(r"$F_n^4/C_{F,m}$")
        plt.ylabel(r"$C_{T,m}/C_{F,m}$")
        plt.title("Prohaska Plot, k="k)
        plt.plot(frac1,frac2)
        plt.plot(lin,func,c="orange",linestyle="dashed")
        plt.grid()
        plt.show()

plot()

np.savetxt("tabel.csv", table_trans, delimiter=",",fmt='%10.3f')

