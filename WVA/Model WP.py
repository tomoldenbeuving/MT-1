import numpy as np
from scipy  import integrate
import math as m
import matplotlib.pyplot as plt
import matplotlib as cm

import Propulsion_system_python_compleet2023_metaanpassingen as model
import Propulsion_system_python_compleet2023 as orgineel


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

v_s_vb = v_m_vb*m.sqrt(aL)
Re_s_vb = (v_s_vb*L_s)/vis_s
Re_m_vb = (v_m_vb*L_m)/vis_m
C_fs_vb = 0.075/(np.log10(Re_s_vb)-2)**2
C_rs_vb = (2*R_tm_vb)/(rho_m*v_m_vb**2*s_m) - 0.075/(np.log10(Re_m_vb)-2)**2
C_ts_vb = C_fs_vb+C_rs_vb
R_ts_vb = 0.5*C_ts_vb*rho_s*v_s_vb**2*s_s 
R_fs_vb = 0.5*C_fs_vb*rho_s*v_s_vb**2*s_s 
R_rs_vb = 0.5*C_rs_vb*rho_s*v_s_vb**2*s_s 


label = np.array(["V_m[m/s]","R_tm[N]","Fr[-]","Re[-]","C_fm[-]","C_tm[-]","Fr^4/C_fm[-]","C_tm/C_fm[-]"])

table_vb = np.array(rekenen(v_m_vb,R_tm_vb))

table = np.array(rekenen(v_m,R_tm))

R_ts = np.nan_to_num(R_ts)
R_ts_vb = np.nan_to_num(R_ts_vb)

table_trans = table_vb.T
def display():
        with np.printoptions(precision=3, suppress=True):
                print(table_trans)


#prohaska rechte lijn
rc = (table_vb[5,5]-table_vb[5,4]+0.0047)/(table_vb[4,5]-table_vb[4,4])
lin = np.arange(0.0,0.21,0.01)
b = table_vb[5,4] - rc*0.1 +0.0185
func = lin*rc+b
k = b-1
k = "%.4f" % k



def plot(var,):
        figure = plt.figure(figsize=(8,6))
        plt.xlabel(r"$F_n^4/C_{F,m}$")
        plt.ylabel(r"$C_{T,m}/C_{F,m}$")
        titel = "Prohaska Plot weerstandsproef, k= "+str(k)
        plt.title(titel)
        plt.plot(var[4],var[5])
        plt.xlim(0,0.25)
        plt.ylim(1.2,1.4)
        plt.scatter(var[4],var[5],label="referentie metingen")
        plt.plot(lin,func,c="orange",linestyle="dashed")
        plt.grid()
        plt.savefig("./Plots/Prohaska met wrijvingslijn.png")

#plot(table_vb)

np.savetxt("tabel.csv", table_trans, delimiter=",",fmt='%10.3f')

R_orgineel = orgineel.R
v_orgineel = orgineel.v_s

R_aangepast = model.R
v_aangepast = model.v_s

fit = np.polyfit(v_s_vb,R_ts_vb,5)
print(fit)
f = np.poly1d(fit)
x = np.linspace(0,7,100)

def plot_R_v(titel):
        figure = plt.figure(figsize=(8,6))
        ax = plt.subplot(111)
        plt.ylabel(r"$R_s \; [N]$")
        plt.xlabel(r"$v_s \; [ms^{-1}]$")
        plt.title("Scheepweerstand $R_s$ over scheepssnelheid $v_s$")
        plt.plot(v_s_vb,R_ts_vb,linestyle="dashed",marker=".",label="totaleweerstand")
        plt.plot(v_s_vb,R_fs_vb,linestyle="dashed",marker=".",label="wrijvingsweerstand")
        plt.plot(v_s_vb,R_rs_vb,linestyle="dashed",marker=".",label="restweerstand")
        plt.plot(v_orgineel,R_orgineel,c="blue",label="model waarden, orgineel")
        plt.plot(v_aangepast,R_aangepast,c="orange",label="model waarden, nieuwe polynoom")
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        titelfig= "./Plots/"+titel+".png"
        plt.grid()
        
        # Shrink current axis's height by 10% on the bottom
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1,
                        box.width, box.height * 0.9])

        # Put a legend below current axis
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
                fancybox=True, shadow=True, ncol=3)

        plt.savefig(titelfig,dpi=1200)

R_v = np.array([R_ts_vb,v_s_vb])
R_v = R_v.T
np.savetxt("tabel R,v.csv", R_v, delimiter=",",fmt='%10.3f')

#plot_R_v("scheepsweerstand met aangepast model")

plot_R_v("voor de pp")

P_theoretisch = model.P_E
W_loss= 711.1+1659.3*(model.n_e/(900/60))
X = model.ov_X_set
Q_f= X * model.m_f_nom * model.LHV

eta_comb =np.zeros(len(P_theoretisch))
eta_td =np.zeros(len(P_theoretisch))
eta_q =np.zeros(len(P_theoretisch))
eta_tot =np.zeros(len(P_theoretisch))
eta_m =np.zeros(len(P_theoretisch))
Q_in =np.zeros(len(P_theoretisch))
Q_loss =np.zeros(len(P_theoretisch))
P_i =np.zeros(len(P_theoretisch)) 
W_i =np.zeros(len(P_theoretisch)) 
W_e =np.zeros(len(P_theoretisch)) 

for k in range(len(P_theoretisch)):
        Q_loss[k]= 1908.8 + 7635.2*(X[k])
        eta_comb[k] = 1
        eta_td[k] = 0.52
        eta_q[k] =(Q_f[k]-Q_loss[k])/Q_f[k]
        W_i[k] = Q_f[k]*eta_comb[k]*eta_td[k]*eta_q[k]
        Q_in[k]=  W_i[k]/eta_td[k]
        P_i[k] = (W_i[k]*model.n_e[k]*model.i)/model.k



        eta_m[k] =  (W_i[k]-W_loss[k])/W_i[k]
        eta_e = eta_comb*eta_m*eta_q*eta_td
        


def plot_P_t(titel):
        fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True, gridspec_kw={'height_ratios': [3, 1]},figsize=(8,6))
        ax1.set_ylabel(r"$P_E \; [kW]$")
        ax1.set_xlabel(r"$t \; [s]$")
        ax1.plot(model.mytime,model.P_E,label="Vermogen")
        ax1.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        ax1.grid()

        ax2.plot(model.mytime,model.ov_Y_set,linestyle="dashed",label="Y parms")
        ax2.plot(model.mytime,model.ov_X_set,linestyle="dashed",label="X parms")
        ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        ax2.grid()

        # Create a single legend object
        handles, labels = [], []
        for ax in fig.axes:
                for h, l in zip(*ax.get_legend_handles_labels()):
                        handles.append(h)
                        labels.append(l)
        legend = fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 0), ncol=3)

        titelfig= "./Plots/"+titel+".png"
        fig.savefig(titelfig, bbox_extra_artists=(legend,), bbox_inches='tight', dpi=1200)

def plot_P_v(titel):
        fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=False, gridspec_kw={'height_ratios': [3, 1]},figsize=(8,6))
        ax1.set_ylabel(r"$P_E \; [kW]$")
        ax1.set_xlabel(r"$v_s \; [ms^{-1}]$")
        ax1.plot(model.v_s,model.P_E,label="Vermogen")
        ax1.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        ax1.grid()

        ax2.plot(model.mytime,model.ov_Y_set,linestyle="dashed",label="Y parms")
        ax2.plot(model.mytime,model.ov_X_set,linestyle="dashed",label="X parms")
        ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        ax2.grid()

        # Create a single legend object
        handles, labels = [], []
        for ax in fig.axes:
                for h, l in zip(*ax.get_legend_handles_labels()):
                        handles.append(h)
                        labels.append(l)
        legend = fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 0), ncol=3)

        titelfig= "./Plots/"+titel+".png"
        fig.savefig(titelfig, bbox_extra_artists=(legend,), bbox_inches='tight',dpi=1200)



def eta_P(titel):
        figure = plt.figure(figsize=(8,6))
        ax = plt.subplot(111)
        plt.ylabel(r"$\eta \; [-]$")
        plt.xlabel(r"$P_e \; [W]$")
        plt.ylim(0,1.1)
        plt.title(titel)
        plt.plot(P_theoretisch[400:],eta_e[400:],label="$\eta_{totaal}$")
#        plt.plot(P_theoretisch[400:],eta_td[400:],  linestyle="dashed",label="$\eta_{td}$")
#        plt.plot(P_theoretisch[400:],eta_m[400:],   linestyle="dashed",label="$\eta_{m}$")
#        plt.plot(P_theoretisch[400:],eta_q[400:],   linestyle="dashed",label="$\eta_{q}$")
#        plt.plot(P_theoretisch[400:],eta_comb[400:],linestyle="dashed",label="$\eta_{comb}$")
        plt.axhline(0.38,linestyle=":",label="$\eta_{model}$")
        plt.ticklabel_format(style='sci', axis='both', scilimits=(0,0))
        titelfig= "./Plots/"+titel+".png"
        plt.grid()
        
        # Shrink current axis's height by 10% on the bottom
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1,
                        box.width, box.height * 0.9])

        # Put a legend below current axis
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
                fancybox=True, shadow=True, ncol=3)

        plt.savefig(titelfig,dpi=1200)


eta_P("eta als funcite van P_e")


v_theoretisch = model.v_s

def eta_v(titel):
        fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=False, gridspec_kw={'height_ratios': [3, 1]},figsize=(8,6))
        ax1.set_ylabel(r"$\eta \; [-]$")
        ax1.set_xlabel(r"$v_s \; [ms^{-1}]$")
        ax1.plot(v_theoretisch[400:],eta_e[400:],label="$\eta_{totaal}$")
        ax1.plot(v_theoretisch[400:],eta_td[400:],  linestyle="dashed",label="$\eta_{td}$")
        ax1.plot(v_theoretisch[400:],eta_m[400:],   linestyle="dashed",label="$\eta_{m}$")
        ax1.plot(v_theoretisch[400:],eta_q[400:],   linestyle="dashed",label="$\eta_{q}$")
        ax1.plot(v_theoretisch[400:],eta_comb[400:],linestyle="dashed",label="$\eta_{comb}$")
        ax1.axhline(0.38,linestyle=":",label="$\eta_{model}$")
        ax1.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        ax1.grid()

        ax2.plot(model.mytime,model.ov_Y_set,linestyle="dashed",label="Y parms")
        ax2.plot(model.mytime,model.ov_X_set,linestyle="dashed",label="X parms")
        ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        ax2.grid()

        # Create a single legend object
        handles, labels = [], []
        for ax in fig.axes:
                for h, l in zip(*ax.get_legend_handles_labels()):
                        handles.append(h)
                        labels.append(l)
        legend = fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 0), ncol=3)

        titelfig= "./Plots/"+titel+".png"
        fig.savefig(titelfig, bbox_extra_artists=(legend,), bbox_inches='tight')

        plt.savefig(titelfig,dpi=1200)

eta_v("eta over v")