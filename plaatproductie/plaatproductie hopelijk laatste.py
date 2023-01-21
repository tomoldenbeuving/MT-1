import matplotlib.pyplot as plt
import numpy as np
import math as m

ss = np.array(np.linspace(0.3,1.0,num=500))
groepsnummer = 2
station  = 5
uren = 8
A_bulb = 0.001780
n_perstation= 3 #aantal pesonen
tp = 0.008
bp = 3
hvrang = 1.25
hspant = 0.16
capaciteit = 22500 + 4/3* 17280


def klein_robot(sg):
    Lp= 12
    A= 144
    Bp = 12
    nzaathout = 4
    aantal_jaar = capaciteit/A 
    nplaat = Bp/bp
    nlas = nplaat -1
    nspant = Bp/ss-nzaathout -1  
    nvrang = Lp/sg
    nkruising = nvrang*(nspant+nzaathout) 
    Llas_plaat = nlas*Lp 
    Llas_spant = nspant*Lp*2  
    Llas_vrang_hori = nvrang*Bp*2  
    Llas_zaathout = nzaathout*Lp*2   
    Llas_vrang_verti = hvrang*nkruising*4 +nspant*hspant*2
    Llas = Llas_plaat + Llas_spant + Llas_vrang_hori + Llas_zaathout + Llas_vrang_verti

    materiaal = 4*(Lp*bp*7800*tp+Bp*75*Lp/sg+(Bp/ss-1)*Lp*A_bulb*7800+Lp*75)+0.5*7800*tp*Llas

    personeel = aantal_jaar*(3933+27*nspant+180*nvrang)

    vastekosten = 106260

    totaal = materiaal + personeel + vastekosten
    return [totaal,materiaal,personeel,vastekosten]
