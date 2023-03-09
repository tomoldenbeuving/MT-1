import numpy as np
from scipy  import integrate
import math as m
import matplotlib.pyplot as plt
import matplotlib as cm
from math import sqrt

np.errstate(divide = 'ignore') 
#v_m = 1.59328

v_m_vb =  np.arange(0.0,1.7,0.1)
v_m_vb= np.delete(v_m_vb,1)
R_tm_vb = np.array([0.0,0.11,0.22,0.41,0.62,0.87,1.18,1.57,2.06,2.62,3.48,4.79,6.22,8.06,11.34,16.65])
v_m = np.array( [0.0,    0.1,    0.2,    0.3,    0.4,    0.6,    0.8,    1.0,    1.2,    1.4,    1.6])
R_tm = np.array([0.0,   0.0354, 0.1022, 0.1782, 0.3359, 1.5856, 2.3528, 3.4945, 5.7248-0.6895,    9.0836-0.6895,    18.079])

#v_s = 13.5*0.51444
L_s = 31.5
L_m = 31.5/19
#R_ts = 100.793*10**3
vis_s = 1.2873E-6
vis_m = 1.0811E-6
rho_s = 1026.6376
rho_m = 998.778
s_s = 272.6
s_m = 272.6/(19**2)
g = 9.81
aL = 19



#R_tm = 0.5*rho_m*var1**2*s_m*(0.075/(m.log10(Re_m)-2)**2 + (2*R_ts)/(rho_s*v_s**2*s_s) - 0.075/(m.log10(Re_s)-2)**2)


def rekenen(var1,var2):

        Fr = var1/m.sqrt(g*L_m) 
        Re = (var1*L_m)/vis_m
        C_fm = 0.075/(np.log10(Re)-2)**2
        C_tm = (var2)/(0.5*rho_m*(var1**2)*s_m)
        frac1 = Fr**4/C_fm
        frac2 = C_tm/C_fm
        return [Fr,Re,C_fm,C_tm,frac1,frac2]


v_s = v_m*m.sqrt(aL)
Re_s = (v_s*L_s)/vis_s
Re_m = (v_m*L_m)/vis_m
C_ts = 0.075/(np.log10(Re_s)-2)**2 + (2*R_tm)/(rho_m*v_m**2*s_m) - 0.075/(np.log10(Re_m)-2)**2

R_ts = 0.5*C_ts*rho_s*v_s**2*s_s 

label = np.array(["V_m[m/s]","R_tm[N]","Fr[-]","Re[-]","C_fm[-]","C_tm[-]","Fr^4/C_fm[-]","C_tm/C_fm[-]"])

table_vb = np.array(rekenen(v_m_vb,R_tm_vb))

table = np.array(rekenen(v_m,R_tm))



table_trans = table_vb.T
def display():
        with np.printoptions(precision=3, suppress=True):
                print(table_trans)


rc = (1.33-1.28)/(0.2-0.1)
lin = np.arange(0.0,0.21,0.01)
b = 1.326359-0.1
func = lin*rc+b
k = b-1
k = "%.4f" % k

def plot(var,var2):
        figure = plt.figure(figsize=(8,5))
        plt.xlabel(r"$F_n^4/C_{F,m}$")
        plt.ylabel(r"$C_{T,m}/C_{F,m}$")
        titel = "Prohaska Plot weerstandsproef"
        plt.title(titel)
        plt.plot(var[4],var[5])
        plt.scatter(var[4],var[5],label="metingen MT-10")
        plt.plot(var2[4],var2[5])
        plt.scatter(var2[4],var2[5],label="referentie metingen")
#        plt.plot(lin,func,c="orange",linestyle="dashed")
        plt.grid()
        plt.legend()
        plt.savefig("Prohaska verpeste WP.png")
        plt.show()

plot(table,table_vb)

np.savetxt("tabel.csv", table_trans, delimiter=",",fmt='%10.3f')


def plot_R_v(var,var2,titel):
        figure = plt.figure(figsize=(8,5))
        plt.ylabel(r"$R_s \; [N]$")
        plt.xlabel(r"$v_s \; [ms^{-1}]$")
        plt.title(titel)
        plt.plot(var,var2)
        plt.scatter(var,var2)
#        plt.plot(lin,func,c="orange",linestyle="dashed")
        titelfig= titel+".png"
        plt.grid()
        plt.savefig(titelfig)
        plt.show()

#plot_R_v(v_s,R_ts,"scheepsweerstand")