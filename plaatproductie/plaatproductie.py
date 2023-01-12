import matplotlib.pyplot as plt
import numpy as np
import math as m
'''
A_klein= 144
A_groot= 288
n_hand= 3
n_robot= 3

'''

#groot
#hand
ss = np.array(np.linspace(0.3,1.0,num=500))
groepsnummer = 2
station  = 5
uren = 8
A_bulb = 0.001780
n= 3
t = 0.008
Bp = 12
bp = 3
Lp= 12*2
A= 144*2
hvrang = 1.25
hspant = 0.16

nzaathout = 8



def totaal(sg):
    nplaat = Bp/bp
    nlas = nplaat -1
    nspant = Bp/ss-nzaathout -1  
    nvrang = Lp/sg
    nkruising = nvrang*(nspant+nzaathout)

    capaciteit = 22500 + 4/3* 17280
    T = 7 + groepsnummer/2
    Llas_plaat = nlas*Lp 
    Llas_spant = nspant*Lp*2  
    Llas_vrang_hori = nvrang*Bp*2  
    Llas_zaathout = nzaathout*Lp*2   
    Llas_vrang_verti = hvrang*nkruising*4 +nspant*hspant*2

    Llas = Llas_plaat + Llas_spant + Llas_vrang_hori + Llas_zaathout + Llas_vrang_verti

    gewicht = 112320*t + 10080/sg + (1123200*A_bulb)/ss -374400*A_bulb +3600+3900*t*Llas
        
    #jaarbasis
    aantal = capaciteit/A

    gewicht_jaar  = aantal*gewicht

    materiaal = gewicht_jaar

    #handstraat
    personeel = 50*n*uren* 1 * 5 * 50

    #personeel_robot = 90*n_robot*uren * 3 * 7 *50

    vastekosten = 70*capaciteit + 10*capaciteit
    #vastekosten_robot = 70*capaciteit + 275000*station + 300000*station

    totaal = materiaal + personeel + vastekosten 
    return totaal
#gewicht_groot = 2*(112320*t + 10080/sg[0] + (11232*A_bulb)/ss -3744*A_bulb +3600)+3900*t*Llas


def plot():
    figure = plt.figure(figsize=(16,9))
    plt.plot(ss,totaal(2), c="orange" ,label="vrangafstand = 2000mm")
    plt.plot(ss,totaal(3), c="blue"   ,label="vrangafstand = 3000mm")
    plt.plot(ss,totaal(4), c="green"  ,label="vrangafstand = 4000mm")
    plt.xlabel("stiffner spacing [mm]")
    plt.ylabel("kosten [euro]")
    titeltje= "Totale Kosten als functie van stiffnerspacing, voor handmatige productie van groot platen"
    plt.title(titeltje)
    plt.legend(loc = "upper right", shadow = True, fontsize="medium")
    #figure.colorbar(surf,shrink=0.5,aspect=5)
    #ax.legend(loc = "lower right", shadow = True, fontsize="large")
    plt.show()

plot()