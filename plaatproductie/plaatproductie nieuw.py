import matplotlib.pyplot as plt
import numpy as np
import math as m

ss = 0.8
groepsnummer = 2
station  = 5
uren = 8
A_bulb = 0.001780
n_perstation= 3 #aantal pesonen
tp = 0.00797
tpmm = 7.97
Bp = 12
bp = 3
Lp= 12
A= 144
hvrang = 1.25
hspant = 0.16
capaciteit = 22500 + 4/3* 17280

'''#hand
personeel = 50/0.35(nplaat + 4 + Llas_plaat/15 +(Llas_vrang_verti/1.2 +(Llas_vrang_hori+Llas_zaathout)/2)*(7.8*tp**2/2000) 1/2*(nspant)+2*(nvrang+nzaathout))
#robot
personeel = 90/0.60(nplaat + 4 + Llas_plaat/30 +(Llas_vrang_verti/2.4 +(Llas_vrang_hori+Llas_zaathout)/4)*(7.8*tp**2/2000) 1/2*(nspant)+2*(nvrang+nzaathout))
'''

class totaal():

    def klein_hand(sg):
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

        materiaal = 35521200*tp + 3415500/sg + 355212000*A_bulb/ss-118404000*A_bulb+1138500+3900*tp*Llas
        urenpplaat = 1/0.35*(nplaat + 4 + Llas_plaat/15 +(Llas_vrang_verti/1.2 +(Llas_vrang_hori+Llas_zaathout+Llas_spant)/2)*(7.8*tpmm**2/2000) +(nspant)+4*(nvrang+nzaathout))
        personeel = aantal_jaar*50* urenpplaat

        vastekosten = 151773.33

        totaal = materiaal + personeel + vastekosten 
        return totaal

    def groot_hand(sg):
        nzaathout = 8
        aantal_jaar = capaciteit/(2*A) 
        nplaat = 2*Bp/bp
        nlas = nplaat -1
        nspant = 2*Bp/ss-nzaathout -1  
        nvrang = Lp/sg
        nkruising = nvrang*(nspant+nzaathout) 
        Llas_plaat = nlas*Lp 
        Llas_spant = nspant*Lp*2  
        Llas_vrang_hori = nvrang*2*Bp*2  
        Llas_zaathout = nzaathout*Lp*2   
        Llas_vrang_verti = hvrang*nkruising*4 +nspant*hspant*2
        Llas = Llas_plaat + Llas_spant + Llas_vrang_hori + Llas_zaathout + Llas_vrang_verti

        materiaal = 35521200*tp + 3415500/sg + 355212000*A_bulb/ss-118404000*A_bulb+1138500+3900*tp*Llas
        urenpplaat = 1/0.35*(nplaat + 4 + Llas_plaat/15 +(Llas_vrang_verti/1.2 +(Llas_vrang_hori+Llas_zaathout+Llas_spant)/2)*(7.8*tpmm**2/2000) +(nspant)+8*(nvrang+nzaathout))

        personeel = aantal_jaar*50*urenpplaat

        vastekosten = 2*151773.33

        totaal = materiaal + personeel + vastekosten 
        return totaal

    def klein_robot(sg):
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

        materiaal = 35521200*tp + 3415500/sg + 355212000*A_bulb/ss-118404000*A_bulb+1138500+3900*tp*Llas

        urenpplaat = 1/0.6*(((Llas_zaathout/2+Llas_vrang_verti/1.2+Llas_vrang_hori/2)*7.8*tpmm**2)/4000)
        personeel = aantal_jaar*50*3*urenpplaat

        vastekosten = 106260+229166.67*((43.7+0.3*nspant+2*nvrang)*137/8400)

        totaal = materiaal + personeel + vastekosten 
        return totaal

    def groot_robot(sg):
        nzaathout = 8
        aantal_jaar = capaciteit/(2*A) 
        nplaat = 2*Bp/bp
        nlas = nplaat -1
        nspant = 2*Bp/ss-nzaathout -1  
        nvrang = Lp/sg
        nkruising = nvrang*(nspant+nzaathout) 
        Llas_plaat = nlas*Lp 
        Llas_spant = nspant*Lp*2  
        Llas_vrang_hori = nvrang*2*Bp*2  
        Llas_zaathout = nzaathout*Lp*2   
        Llas_vrang_verti = hvrang*nkruising*4 +nspant*hspant*2
        Llas = Llas_plaat + Llas_spant + Llas_vrang_hori + Llas_zaathout + Llas_vrang_verti

        materiaal = 35521200*tp + 3415500/sg + 355212000*A_bulb/ss-118404000*A_bulb+1138500+3900*tp*Llas

        urenpplaat = 1/0.6*((Llas_zaathout+Llas_vrang_verti+Llas_vrang_hori)*7.8*tpmm**2)/800
        personeel = aantal_jaar*50*3*urenpplaat

        vastekosten = 106260+250000*((88.5+0.3*nspant+4*nvrang)*159/8400)

        totaal = materiaal + personeel + vastekosten 
        return totaal

totaal.klein_robot(4)
totaal.klein_hand(4)

