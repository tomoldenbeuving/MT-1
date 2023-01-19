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
Bp = 12
bp = 3
Lp= 12
A= 144
hvrang = 1.25
hspant = 0.16
capaciteit = 22500 + 4/3* 17280

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
        Llas_plaat = nlas*Lp 
        Llas_spant = nspant*Lp*2  
        Llas_vrang_hori = nvrang*Bp*2  
        Llas_zaathout = nzaathout*Lp*2   
        Llas_vrang_verti = hvrang*nkruising*4 +nspant*hspant*2
        Llas = Llas_plaat + Llas_spant + Llas_vrang_hori + Llas_zaathout + Llas_vrang_verti

        materiaal = 35521200*tp + 3415500/sg + 3552120*A_bulb/ss - 7488000*A_bulb + 1138500+3900*tp*Llas

        personeel = aantal_jaar*(150+37.5/ss+600/sg)

        vastekosten = 3643200/30

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

        materiaal = 35521200*tp + 3415500/sg + 3552120*2*A_bulb/sg - 7488000*A_bulb + 1138500+3900*tp*Llas

        personeel = aantal_jaar*(150+15/ss+600/sg)

        vastekosten = 3643200/30

        totaal = materiaal + personeel + vastekosten 
        return totaal

    def klein_robot_5(sg):
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

        materiaal = 35521200*tp + 3415500/sg + 3552120*A_bulb/sg - 7488000*A_bulb + 1138500+3900*tp*Llas

        personeel = aantal_jaar*(45+81/ss+2160/sg)

        vastekosten = 1375000*((0.5+0.9/ss+24/sg*317)/8760)+3187800/30

        totaal = materiaal + personeel + vastekosten 
        return totaal

    def groot_robot_4(sg):
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

        materiaal = 35521200*tp + 3415500/sg + 3552120*2*A_bulb/sg - 7488000*A_bulb + 1138500+3900*tp*Llas

        personeel = aantal_jaar*(45+81/ss+4320/sg)

        vastekosten = 1200000*((0.5+0.9/ss+24/sg*159)/8760)+3187800/30

        totaal = materiaal + personeel + vastekosten 
        return totaal

    def klein_robot_4(sg):
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

        materiaal = 35521200*tp + 3415500/sg + 3552120*A_bulb/sg - 7488000*A_bulb + 1138500+3900*tp*Llas

        personeel = aantal_jaar*(45+81/ss+2160/sg)

        vastekosten = 1100000*((0.5+0.9/ss+24/sg*317)/8760)+3187800/30

        totaal = materiaal + personeel + vastekosten 
        return totaal

    def groot_robot_5(sg):
        nzaathout = 8
        aantal_jaar = capaciteit/(2*A)
        nplaat = Bp/bp
        nlas = nplaat -1
        nspant = Bp/ss-nzaathout -1  
        nvrang = 2*Lp/sg
        nkruising = nvrang*(nspant+nzaathout) 
        Llas_plaat = nlas*2*Lp 
        Llas_spant = nspant*2*Lp*2  
        Llas_vrang_hori = nvrang*Bp*2  
        Llas_zaathout = nzaathout*2*Lp*2   
        Llas_vrang_verti = hvrang*nkruising*4 +nspant*hspant*2
        Llas = Llas_plaat + Llas_spant + Llas_vrang_hori + Llas_zaathout + Llas_vrang_verti

        materiaal = 35521200*tp + 3415500/sg + 3552120*2*A_bulb/sg - 7488000*A_bulb + 1138500+3900*tp*Llas

        personeel = aantal_jaar*(45+81/ss+4320/sg)

        vastekosten = 1500000*((0.5+0.9/ss+24/sg*159)/8760)+3187800/30

        totaal = materiaal + personeel + vastekosten 
        return totaal

class materiaal():

    def klein_hand(sg):
        nzaathout = 4
        aantal_jaar = capaciteit/A 
        nplaat = Bp/bp
        nlas = nplaat -1
        nspant = Bp/ss-nzaathout -1  
        nvrang = Lp/sg
        nkruising = nvrang*(nspant+nzaathout)
        Llas_plaat = nlas*Lp     
        Llas_plaat = nlas*Lp 
        Llas_spant = nspant*Lp*2  
        Llas_vrang_hori = nvrang*Bp*2  
        Llas_zaathout = nzaathout*Lp*2   
        Llas_vrang_verti = hvrang*nkruising*4 +nspant*hspant*2
        Llas = Llas_plaat + Llas_spant + Llas_vrang_hori + Llas_zaathout + Llas_vrang_verti

        materiaal = 35521200*tp + 3415500/sg + 3552120*A_bulb/ss - 7488000*A_bulb + 1138500+3900*tp*Llas

        personeel = aantal_jaar*(150+37.5/ss+600/sg)

        vastekosten = 3643200/30

        totaal = materiaal
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

        materiaal = 35521200*tp + 3415500/sg + 3552120*2*A_bulb/sg - 7488000*A_bulb + 1138500+3900*tp*Llas

        personeel = aantal_jaar*(150+15/ss+600/sg)

        vastekosten = 3643200/30

        totaal = materiaal 
        return totaal

    def klein_robot_5(sg):
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

        materiaal = 35521200*tp + 3415500/sg + 3552120*A_bulb/sg - 7488000*A_bulb + 1138500+3900*tp*Llas

        personeel = aantal_jaar*(45+81/ss+2160/sg)

        vastekosten = 1375000*((0.5+0.9/ss+24/sg*317)/8760)+3187800/30

        totaal = materiaal
        return totaal

    def groot_robot_4(sg):
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

        materiaal = 35521200*tp + 3415500/sg + 3552120*2*A_bulb/sg - 7488000*A_bulb + 1138500+3900*tp*Llas

        personeel = aantal_jaar*(45+81/ss+4320/sg)

        vastekosten = 1200000*((0.5+0.9/ss+24/sg*159)/8760)+3187800/30

        totaal = materiaal 
        return totaal

    def klein_robot_4(sg):
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

        materiaal = 35521200*tp + 3415500/sg + 3552120*A_bulb/sg - 7488000*A_bulb + 1138500+3900*tp*Llas

        personeel = aantal_jaar*(45+81/ss+2160/sg)

        vastekosten = 1100000*((0.5+0.9/ss+24/sg*317)/8760)+3187800/30

        totaal = materiaal
        return totaal

    def groot_robot_5(sg):
        nzaathout = 8
        aantal_jaar = capaciteit/(2*A)
        nplaat = Bp/bp
        nlas = nplaat -1
        nspant = Bp/ss-nzaathout -1  
        nvrang = 2*Lp/sg
        nkruising = nvrang*(nspant+nzaathout) 
        Llas_plaat = nlas*2*Lp 
        Llas_spant = nspant*2*Lp*2  
        Llas_vrang_hori = nvrang*Bp*2  
        Llas_zaathout = nzaathout*2*Lp*2   
        Llas_vrang_verti = hvrang*nkruising*4 +nspant*hspant*2
        Llas = Llas_plaat + Llas_spant + Llas_vrang_hori + Llas_zaathout + Llas_vrang_verti

        materiaal = 35521200*tp + 3415500/sg + 3552120*2*A_bulb/sg - 7488000*A_bulb + 1138500+3900*tp*Llas

        personeel = aantal_jaar*(45+81/ss+4320/sg)

        vastekosten = 1500000*((0.5+0.9/ss+24/sg*159)/8760)+3187800/30

        totaal = materiaal
        return totaal

class personeel():

    def klein_hand(sg):
        nzaathout = 4
        aantal_jaar = capaciteit/A 
        nplaat = Bp/bp
        nlas = nplaat -1
        nspant = Bp/ss-nzaathout -1  
        nvrang = Lp/sg
        nkruising = nvrang*(nspant+nzaathout)
        Llas_plaat = nlas*Lp     
        Llas_plaat = nlas*Lp 
        Llas_spant = nspant*Lp*2  
        Llas_vrang_hori = nvrang*Bp*2  
        Llas_zaathout = nzaathout*Lp*2   
        Llas_vrang_verti = hvrang*nkruising*4 +nspant*hspant*2
        Llas = Llas_plaat + Llas_spant + Llas_vrang_hori + Llas_zaathout + Llas_vrang_verti

        materiaal = 35521200*tp + 3415500/sg + 3552120*A_bulb/ss - 7488000*A_bulb + 1138500+3900*tp*Llas

        personeel = aantal_jaar*(150+37.5/ss+600/sg)

        vastekosten = 3643200/30

        totaal = personeel
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

        materiaal = 35521200*tp + 3415500/sg + 3552120*2*A_bulb/sg - 7488000*A_bulb + 1138500+3900*tp*Llas

        personeel = aantal_jaar*(150+15/ss+600/sg)

        vastekosten = 3643200/30

        totaal = personeel 
        return totaal

    def klein_robot_5(sg):
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

        materiaal = 35521200*tp + 3415500/sg + 3552120*A_bulb/sg - 7488000*A_bulb + 1138500+3900*tp*Llas

        personeel = aantal_jaar*(45+81/ss+2160/sg)

        vastekosten = 1375000*((0.5+0.9/ss+24/sg*317)/8760)+3187800/30

        totaal = personeel
        return totaal

    def groot_robot_4(sg):
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

        materiaal = 35521200*tp + 3415500/sg + 3552120*2*A_bulb/sg - 7488000*A_bulb + 1138500+3900*tp*Llas

        personeel = aantal_jaar*(45+81/ss+4320/sg)

        vastekosten = 1200000*((0.5+0.9/ss+24/sg*159)/8760)+3187800/30

        totaal = personeel 
        return totaal

    def klein_robot_4(sg):
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

        materiaal = 35521200*tp + 3415500/sg + 3552120*A_bulb/sg - 7488000*A_bulb + 1138500+3900*tp*Llas

        personeel = aantal_jaar*(45+81/ss+2160/sg)

        vastekosten = 1100000*((0.5+0.9/ss+24/sg*317)/8760)+3187800/30

        totaal = personeel
        return totaal

    def groot_robot_5(sg):
        nzaathout = 8
        aantal_jaar = capaciteit/(2*A)
        nplaat = Bp/bp
        nlas = nplaat -1
        nspant = Bp/ss-nzaathout -1  
        nvrang = 2*Lp/sg
        nkruising = nvrang*(nspant+nzaathout) 
        Llas_plaat = nlas*2*Lp 
        Llas_spant = nspant*2*Lp*2  
        Llas_vrang_hori = nvrang*Bp*2  
        Llas_zaathout = nzaathout*2*Lp*2   
        Llas_vrang_verti = hvrang*nkruising*4 +nspant*hspant*2
        Llas = Llas_plaat + Llas_spant + Llas_vrang_hori + Llas_zaathout + Llas_vrang_verti

        materiaal = 35521200*tp + 3415500/sg + 3552120*2*A_bulb/sg - 7488000*A_bulb + 1138500+3900*tp*Llas

        personeel = aantal_jaar*(45+81/ss+4320/sg)

        vastekosten = 1500000*((0.5+0.9/ss+24/sg*159)/8760)+3187800/30

        totaal = personeel
        return totaal

class vastekosten():

    def klein_hand(sg):
        nzaathout = 4
        aantal_jaar = capaciteit/A 
        nplaat = Bp/bp
        nlas = nplaat -1
        nspant = Bp/ss-nzaathout -1  
        nvrang = Lp/sg
        nkruising = nvrang*(nspant+nzaathout)
        Llas_plaat = nlas*Lp     
        Llas_plaat = nlas*Lp 
        Llas_spant = nspant*Lp*2  
        Llas_vrang_hori = nvrang*Bp*2  
        Llas_zaathout = nzaathout*Lp*2   
        Llas_vrang_verti = hvrang*nkruising*4 +nspant*hspant*2
        Llas = Llas_plaat + Llas_spant + Llas_vrang_hori + Llas_zaathout + Llas_vrang_verti

        materiaal = 35521200*tp + 3415500/sg + 3552120*A_bulb/ss - 7488000*A_bulb + 1138500+3900*tp*Llas

        personeel = aantal_jaar*(150+37.5/ss+600/sg)

        vastekosten = 3643200/30

        totaal = vastekosten*ss/ss
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

        materiaal = 35521200*tp + 3415500/sg + 3552120*2*A_bulb/sg - 7488000*A_bulb + 1138500+3900*tp*Llas

        personeel = aantal_jaar*(150+15/ss+600/sg)

        vastekosten = 3643200/30

        totaal = vastekosten*ss/ss
        return totaal

    def klein_robot_5(sg):
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

        materiaal = 35521200*tp + 3415500/sg + 3552120*A_bulb/sg - 7488000*A_bulb + 1138500+3900*tp*Llas

        personeel = aantal_jaar*(45+81/ss+2160/sg)

        vastekosten = 1375000*((0.5+0.9/ss+24/sg*317)/8760)+3187800/30

        totaal = vastekosten*ss/ss
        return totaal

    def groot_robot_4(sg):
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

        materiaal = 35521200*tp + 3415500/sg + 3552120*2*A_bulb/sg - 7488000*A_bulb + 1138500+3900*tp*Llas

        personeel = aantal_jaar*(45+81/ss+4320/sg)

        vastekosten = 1200000*((0.5+0.9/ss+24/sg*159)/8760)+3187800/30

        totaal = vastekosten *ss/ss
        return totaal

    def klein_robot_4(sg):
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

        materiaal = 35521200*tp + 3415500/sg + 3552120*A_bulb/sg - 7488000*A_bulb + 1138500+3900*tp*Llas

        personeel = aantal_jaar*(45+81/ss+2160/sg)

        vastekosten = 1100000*((0.5+0.9/ss+24/sg*317)/8760)+3187800/30

        totaal = vastekosten*ss/ss
        return totaal

    def groot_robot_5(sg):
        nzaathout = 8
        aantal_jaar = capaciteit/(2*A)
        nplaat = Bp/bp
        nlas = nplaat -1
        nspant = Bp/ss-nzaathout -1  
        nvrang = 2*Lp/sg
        nkruising = nvrang*(nspant+nzaathout) 
        Llas_plaat = nlas*2*Lp 
        Llas_spant = nspant*2*Lp*2  
        Llas_vrang_hori = nvrang*Bp*2  
        Llas_zaathout = nzaathout*2*Lp*2   
        Llas_vrang_verti = hvrang*nkruising*4 +nspant*hspant*2
        Llas = Llas_plaat + Llas_spant + Llas_vrang_hori + Llas_zaathout + Llas_vrang_verti

        materiaal = 35521200*tp + 3415500/sg + 3552120*2*A_bulb/sg - 7488000*A_bulb + 1138500+3900*tp*Llas

        personeel = aantal_jaar*(45+81/ss+4320/sg)

        vastekosten = 1500000*((0.5+0.9/ss+24/sg*159)/8760)+3187800/30

        totaal = vastekosten*ss/ss
        return totaal


def plot(klein,groot,titel):
    figure = plt.figure(figsize=(10,8))
    plt.plot(ss,klein(2), c="orange"    ,label="kleine platen, vrangafstand = 2m")
    plt.plot(ss,klein(3), c="blue"      ,label="\" vrangafstand = 3m")
    plt.plot(ss,klein(4), c="green"     ,label="\" vrangafstand = 4m")
    plt.plot(ss,groot(2), c="red"       ,label="grote platen, vrangafstand = 2m")
    plt.plot(ss,groot(3), c="yellow"    ,label="\" vrangafstand = 3m")
    plt.plot(ss,groot(4), c="black"     ,label="\" vrangafstand = 4m")
    plt.xlabel("verstijver spacing [m]")
    plt.ylabel("kosten [euro]")
    titeltje= "Functie van verstijver spacing, voor "+titel
    plt.title(titeltje)
    plt.legend(loc = "best", shadow = True, fontsize="small")
    figure.savefig("./plaatproductie/"+titel+".png")
    #figure.colorbar(surf,shrink=0.5,aspect=5)
    #ax.legend(loc = "lower right", shadow = True, fontsize="large")


def plot_test(self,titel):
    fig, ax = plt.subplots(figsize=(16,9))
    fig.subplots_adjust(right=0.75)

    twin1 = ax.twinx()
    twin2 = ax.twinx()

    # Offset the right spine of twin2.  The ticks and label have already been
    # placed on the right by twinx above.
    twin2.spines.right.set_position(("axes", 1.2))

    p1, = ax.plot(ss,self(2), "b", label="vrang = 2000 mm")
    p2, = twin1.plot(ss,self(3), "r:", label="vrang = 3000 mm")
    p3, = twin2.plot(ss,self(4), "g--", label="vrang = 4000 mm")

    ax.set_xlabel("verstijver spacing")
    ax.set_ylabel("2000 mm")
    twin1.set_ylabel("3000 mm")
    twin2.set_ylabel("4000 mm")

    ax.yaxis.label.set_color(p1.get_color())
    twin1.yaxis.label.set_color(p2.get_color())
    twin2.yaxis.label.set_color(p3.get_color())

    tkw = dict(size=4, width=1.5)
    ax.tick_params(axis='y', colors=p1.get_color(), **tkw)
    twin1.tick_params(axis='y', colors=p2.get_color(), **tkw)
    twin2.tick_params(axis='y', colors=p3.get_color(), **tkw)
    ax.tick_params(axis='x', **tkw)
    titeltje= "Totale Kosten als functie van stiffnerspacing, voor "+titel+"met variabele y-as"
    ax.set_title(titeltje)

    ax.set_yticks(np.arange(min(self(2)),max(self(2)),0.01E6))
    twin1.set_yticks(np.arange(min(self(3)),max(self(3)),0.01E6))
    twin2.set_yticks(np.arange(min(self(4)),max(self(4)),0.01E6))
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

    # Put a legend below current axis
    ax.legend(handles=[p1, p2, p3],loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=True, shadow=True, ncol=5)
    fig.savefig("./plaatproductie/"+titel+" 3-in-1.png")
    plt.show()

def bar_plot():
    materiaal_tup = (min(materiaal.klein_hand(4)),min(materiaal.groot_hand(4)),min(materiaal.klein_robot_5(4)),min(materiaal.groot_robot_5(4)))
    personeel_tup = (min(personeel.klein_hand(4)),min(personeel.groot_hand(4)),min(personeel.klein_robot_5(4)),min(personeel.groot_robot_5(4)))
    vastekosten_tup = (min(vastekosten.klein_hand(4)),min(vastekosten.groot_hand(4)),min(vastekosten.klein_robot_5(4)),min(vastekosten.groot_robot_5(4)))
    figure = plt.figure(figsize=(10,8))
    ind = np.arange(4)
    plt.bar(ind, np.array(materiaal_tup), 0.35,    color="red", label="materiaal")
    plt.bar(ind, np.array(personeel_tup),  0.35,   bottom=np.array(materiaal_tup),   color="green", label="personeel")
    plt.bar(ind, np.array(vastekosten_tup), 0.35,  bottom=np.array(personeel_tup)+np.array(materiaal_tup),    color="blue", label="vastekosten")
    plt.xticks(ind,["klein, hand","groot, hand","klein, robot","groot, robot"])
    plt.ylabel("kosten [euro]")
    titeltje= "Minimale Kosten in de vier scenarios"
    plt.title(titeltje)
    plt.legend(loc = "best", shadow = True, fontsize="small")
    figure.savefig("./plaatproductie/barplot.png")

plot(totaal.klein_robot_5, totaal.groot_robot_5,"totale kosten robot")
plot(totaal.klein_hand, totaal.groot_hand,"totale kosten hand")


plot(materiaal.klein_robot_5, materiaal.groot_robot_5,"materiaal kosten ")

plot(vastekosten.klein_robot_5, vastekosten.groot_robot_5,"vastekosten robot")
plot(vastekosten.klein_hand, vastekosten.groot_hand,"vastekosten hand")


plot(personeel.klein_robot_5, personeel.groot_robot_5,"personeels kosten robot")
plot(personeel.klein_hand, personeel.groot_hand,"personeels kosten hand")

bar_plot()