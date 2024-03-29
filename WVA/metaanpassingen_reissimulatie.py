# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 11:02:26 2017
                                                                      
    Viskotter simulation file                                         
    Version 1.0H
    J. Rodrigues Monteiro, based on matlab code from P. de Vos                                                         
    Delft University of Technology                                    
    3ME / MTT / SDPO / ME                                             
                                                                      
History:
    20171108I: initial python version    JRM
    20200108J: simps integration         EU
               no graphing endpoits...   EU
    20200228K: simps correctie           EU
    20230201L: back to trapz and 5 days  EU          
"""
import numpy as np
import math
import matplotlib.pyplot as plt
import time
#ik heb iets aangepast

#from scipy import integrate

# ----------- parameters for simulation --------------------------------------

tmax = 8*3600           # simulation time [s]
dt = 1                  # timestep [s]

# fuel properties
LHV = 42700             # Lower Heating Value [kJ/kg]
print('fuel properties loaded')

# water properties
rho_sw = 1025           # density of seawater [kg/m3]
print('water properties loaded')

# ship data
m_ship = 358000         # ship mass [kg]
c1 = 1500       
v_s0 = 0       # resistance coefficient c1 in R = c1*vs^2
#v_s0 = 6.5430           # ship design speed [m/s]
t = 0.1600              # thrust deduction factor[-]
w = 0.2000              # wake factor [-]
print('ship data loaded')

# propellor data
D_p = 3                 # diameter of propellor [m]
K_T_a = -0.3821         # factor a in K_T = a*J + b [-]
K_T_b = 0.2885          # factor b in K_T = a*J + b [-]
K_Q_a = -0.03346        # factor a in K_Q = a*J + b [-]
K_Q_b = 0.0308          # factor b in K_Q = a*J + b [-]
eta_R = 1.0100          # relative rotative efficiency [-]
print('propellor data loaded')

# engine data
m_f_nom = 1.314762      # nominal fuel injection [g]
eta_e = 0.3800          # nominal engine efficiency [-]
i = 6                   # number of cylinders [-]
k_es = 2                # k-factor for engines based on nr.of strokes per cycle
P_b = np.zeros(tmax)    # engine power [kW]
P_b[0] = 960            # Nominal engine power [kW]
M_b = np.zeros(tmax)    # engine torque [Nm]
M_b[0] = P_b[0]*1000/2/math.pi/(900/60)  # ([P_b*1000/2/math.pi/n_eng_nom])
print('engine data loaded')

# gearbox data
eta_TRM = 0.9500        # transmission efficiency [-]
i_gb = 4.2100           # gearbox ratio [-]
I_tot = 200             # total mass of inertia of propulsion system [kg*m^2]
print('gearbox data loaded')

# initial values
in_p = 3.2830           # initial rpm
iv_t_control =  np.array([0,    tmax*8/64,      tmax*8/64+1,    tmax*56/64,     tmax*56/64+1,   tmax])
X_parms =       np.array([0.9,  0.9,            0.9,            0.9,            0.9,            0.9])   # % maximum fuelrack
Y_parms =       np.array([1.0,  1.0,            106.187,        106.187,        1.05,           1.05])               # disturbance factor


# simulation control parameters
xvals = np.linspace(0, tmax-1, tmax)
ov_X_set = np.interp(xvals, iv_t_control, X_parms)
ov_Y_set = np.interp(xvals, iv_t_control, Y_parms)

# --------- Start van de funtie definities

def R_schip(v, Y):
      weerstand = Y*(56.32937638*v**5-764.50436608*v**4  + 3868.76371477*v**3 -7618.88519419*v**2 +5851.40183619*v  - 248.82429537)
      return weerstand


# -------- Make arrays -------------------------------------------------------

# Time
mytime = np.linspace(0, tmax-1, tmax)
# Velocity of the ship [m/s]
v_s = np.zeros(tmax)
v_s[0] = v_s0
# Distance traveled [m]
s = np.zeros(tmax)
# Advance velocity [m/s]
v_a = np.zeros(tmax)
v_a[0] = (1-w) * v_s0
# Rpm propellor [Hz]
n_p = np.zeros(tmax)
n_p[0] = in_p
# Rpm diesel engine [Hz]
n_e = np.zeros(tmax)
n_e[0] = 900/60         # Nominal engine speed in rotations per second [Hz]
# Resistance [N]
R = np.zeros(tmax)
Y = ov_Y_set[0]
R[0] = R_schip(v_s0, Y)
# Acceleration ship [m/s^2]
sum_a = np.zeros(tmax)


# Acceleration propellor[1/s^2]
sum_dnpdt = np.zeros(tmax)
m_flux_f = np.zeros(tmax)
out_fc = np.zeros(tmax)

M_Trm = np.zeros(tmax)            # M_B * i_gb * eta_TRM
KT = np.zeros(tmax)               # Thrust coefficient [-]
KQ = np.zeros(tmax)               # Torque coefficient [-]
Rsp = np.zeros(tmax)              # Resistance propelled situation [N]
F_prop = np.zeros(tmax)           # Thrust power [N]
M_prop = np.zeros(tmax)           # Torque [Nm]
P_O = np.zeros(tmax)              # Open water propellor power
P_p = np.zeros(tmax)              # Propellor power [kW]
P_b = np.zeros(tmax)              # Engine brake power [kW]
P_T = np.zeros(tmax)              # Thrust power [kW]
P_E = np.zeros(tmax)              # Engine power [kW]
J = np.zeros(tmax)                # Advance ratio [-]
W_loss= np.zeros(tmax)
W_i = np.zeros(tmax)
X= np.zeros(tmax)
Q_f= np.zeros(tmax)
W_e=np.zeros(tmax)
eta_i=np.zeros(tmax)
eta_m=np.zeros(tmax)
eta_q=np.zeros(tmax)

X[0]= ov_X_set[0]
Q_f[0]= X[0] * m_f_nom * LHV
W_loss[0]= 711.1 +1659.3*(n_e[0]/15)
Q_f[0] = X[0] * m_f_nom * LHV

W_e[0]= (Q_f[0]) * eta_i[0] * eta_m[0]
eta_q[0]=(Q_f[0]-(1908.8 + 7635.2*(X[0]/0.85)))/Q_f[0]


P_E[0] = R[0]*v_s0




# ------------- Run simulation -----------------------------------------------
start = time.perf_counter() 
 
for k in range(tmax-1):
    ov_X_set = np.clip(ov_X_set,0.2,1)
    # advance ratio
    J[k+1] = ((v_a[k] / n_p[k]) / D_p)
    # Thrust and torque
    F_prop[k] = ((((J[k+1] * K_T_a) + K_T_b) *
                  n_p[k] ** 2) * rho_sw * D_p ** 4)
    M_prop[k] = (((((J[k+1] * K_Q_a) + K_Q_b) *
                  n_p[k] ** 2) * rho_sw * D_p ** 5) / eta_R)
    KT[0] = -0.16026829*J[0]**2 + -0.28308796*J[0]  +0.27711417
    KQ[0] = -0.19249704*J[0]**2 + -0.19043507*J[0]+  0.28027716
    KT[k+1] = -0.16026829*J[k+1]**2 + -0.28308796*J[k+1]  +0.27711417
    KQ[k+1] = -0.19249704*J[k+1]**2 + -0.19043507*J[k+1]+  0.28027716
    P_O[k+1] = ((((J[k+1] * K_Q_a) + K_Q_b) *
                n_p[k] ** 2) * rho_sw * D_p ** 5) * n_p[k] * 2 * math.pi
    P_p[k+1] = M_prop[k] * n_p[k] * 2 * math.pi
    # Calculate acceleration from resulting force --> ship speed & tr.distance
    sum_a[k+1] = ((F_prop[k] - (R[k] / (1-t)))/m_ship)
    v_s[k+1]  = (np.trapz(sum_a[k:k+2], dx=0.01)) + v_s[k]
    #v_s[k+1] = v_s_new
    Rsp[k+1] = R[k] / (1-t)
    
    
    # Traveled distance
    s[k+1] = s[k] + v_s[k+1] * dt
    
    
    # Advance velocity
    v_a[k+1] = v_s[k+1] * (1 - w)
    P_T[k+1] = F_prop[k] * v_a[k+1]
    
    
    # Resistance
    Y = ov_Y_set[k]
    R[k+1] = R_schip( v_s[k+1], Y)
    P_E[0] = v_s[0]*R[0]
    P_E[k+1] = v_s[k+1]*R[k+1]
    
    
    # Calculate acceleration from resulting force --> propellor np
    sum_dnpdt[k+1] = ((M_b[k] * i_gb * eta_TRM) - M_prop[k])/(2*math.pi*I_tot)
    n_p[k+1] = np.trapz(sum_dnpdt[k:k+2], dx=0.01) + n_p[k]
    
    
    # Engine speed
    n_e[k+1] = n_p[k+1] * i_gb
    
    
    # Fuel rack
    X[k+1] = ov_X_set[k+1]
    m_flux_f[0] = (X[0] * m_f_nom * n_e[0]) * i / k_es
    m_flux_f[k+1] = (X[k+1] * m_f_nom * n_e[k+1]) * i / k_es
    # Fuel consumption
    out_fc[k+1] =  np.trapz(m_flux_f[:k+2], dx=0.01)+out_fc[0]
   
    
    Q_f[k+1] = X[k+1] * m_f_nom * LHV
    etaTD = 0.52
    etaComb = 1
    eta_q[k+1] = (Q_f[k+1]-(1908.8 + 7635.2*(X[k+1])))/Q_f[k+1]
    eta_q[0] = (Q_f[0]-(1908.8 + 7635.2*(X[0])))/Q_f[0]
    eta_i[0]= etaComb*eta_q[0]*etaTD
    eta_i[k+1] = etaComb*eta_q[k+1]*etaTD
    W_i[k+1] = Q_f[k+1]*eta_i[k+1]
    W_i[0] = Q_f[0]*eta_i[0]
    W_loss[k+1] = 711.1 +1659.3*(n_e[k+1]/15)
    eta_m[0]= (W_i[0]-(W_loss[0]))/W_i[0]
    eta_m[k+1] = (W_i[k+1]-(W_loss[k+1]))/W_i[k+1]
    W_e[0]= (Q_f[0]) * eta_i[0] * eta_m[0]
    W_e[k+1] = (Q_f[k+1]) * eta_i[k+1] * eta_m[k+1]
    # Brake power
    P_b[k+1] = (W_e[k+1] * n_e[k+1]*i) / k_es
    # Engine torque
    M_b[k+1] = P_b[k+1] / (2 * math.pi * n_e[k+1])
    M_Trm[0] = M_b[0] * i_gb * eta_TRM
    M_Trm[k+1] = M_b[k+1] * i_gb * eta_TRM


# EU just to be sure
v_s[0]=v_s0


eta_q = np.delete(eta_q , [0,10])
eta_m = np.delete(eta_m , [0,10])
# -------------- Plot Figure -------------------------------------------------

# create figure with four subplots
fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(4, 1, 1)  # fig.add_subplot(#rows, #cols, #plot)
ax1.plot(mytime, v_s)
ax1.set(title='Ship Propulsion Output',
        ylabel='Ship speed [m/s]',
        xlabel='Time [s]')
ax1.grid()
ax2 = fig.add_subplot(4, 1, 2)
ax2.plot(mytime, s)
ax2.set(ylabel='Distance traveled [m]',
        xlabel='Time [s]')
ax2.grid()
ax3 = fig.add_subplot(4, 1, 3)
ax3.plot(mytime, out_fc)
ax3.set(ylabel='Fuel consumed [g]',
        xlabel='Time [s]')
ax3.grid()
ax4 = fig.add_subplot(4, 1, 4)
ax4.plot(mytime, ov_X_set)
ax4.set(ylabel='Fuel rack [-]',
        xlabel='Time [s]')
ax4.grid()
fig.tight_layout()


fig.savefig('test_plot1.svg')
fig.savefig('test_plot1.png')
print('run time:',time.perf_counter()-start,'seconden')

np.savetxt("R_aangepast.csv", R, delimiter=",",fmt='%10.3f')
np.savetxt("v_aangepast.csv", v_s, delimiter=",",fmt='%10.3f')



