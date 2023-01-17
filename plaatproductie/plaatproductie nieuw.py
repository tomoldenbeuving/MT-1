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
nzaathout = 8 
capaciteit = 22500 + 4/3* 17280

class totaal():

    def klein_hand(sg):
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

        personeel = capaciteit*(150+37.5/ss+600/sg)

        vastekosten = 3643200

        totaal = materiaal + personeel + vastekosten 
        return totaal

    def groot_hand(sg):
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

        personeel = capaciteit*(150+15/ss+600/sg)

        vastekosten = 3643200

        totaal = materiaal + personeel + vastekosten 
        return totaal

    def klein_robot_5(sg):
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

        personeel = capaciteit*(45+81/ss+2160/sg)

        vastekosten = 1375000*((0.5+0.9/ss+24/sg*317)/8760)+3187800

        totaal = materiaal + personeel + vastekosten 
        return totaal

    def groot_robot_4(sg):
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

        personeel = capaciteit*(45+81/ss+4320/sg)

        vastekosten = 1200000*((0.5+0.9/ss+24/sg*159)/8760)+3187800

        totaal = materiaal + personeel + vastekosten 
        return totaal

    def klein_robot_4(sg):
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

        personeel = capaciteit*(45+81/ss+2160/sg)

        vastekosten = 1100000*((0.5+0.9/ss+24/sg*317)/8760)+3187800

        totaal = materiaal + personeel + vastekosten 
        return totaal

    def groot_robot_5(sg):
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

        personeel = capaciteit*(45+81/ss+4320/sg)

        vastekosten = 1500000*((0.5+0.9/ss+24/sg*159)/8760)+3187800

        totaal = materiaal + personeel + vastekosten 
        return totaal


def plot(self,titel):
    figure = plt.figure(figsize=(16,9))
    plt.plot(ss,self(2), c="orange" ,label="vrangafstand = 2000mm")
    plt.plot(ss,self(3), c="blue"   ,label="vrangafstand = 3000mm")
    plt.plot(ss,self(4), c="green"  ,label="vrangafstand = 4000mm")
    plt.xlabel("stiffner spacing [m]")
    plt.ylabel("kosten [euro]")
    titeltje= "Totale Kosten als functie van stiffnerspacing, voor "+titel
    plt.title(titeltje)
    plt.legend(loc = "upper right", shadow = True, fontsize="medium")
    figure.savefig("./plaatproductie/"+titel+".png")
    #figure.colorbar(surf,shrink=0.5,aspect=5)
    #ax.legend(loc = "lower right", shadow = True, fontsize="large")

plot(totaal.groot_robot_5,"robot, groot, 5 stations")
plot(totaal.groot_robot_4,"robot, groot, 4 stations")
plot(totaal.klein_robot_5,"robot, klein, 5 stations")
plot(totaal.klein_robot_4,"robot, klein, 4 stations")
plot(totaal.klein_hand,"hand, klein")
plot(totaal.groot_hand,"hand, groot")

