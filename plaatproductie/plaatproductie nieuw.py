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

        vastekosten = 3643200

        totaal = materiaal + personeel + vastekosten 
        return totaal

    def groot_hand(sg):
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

        personeel = aantal_jaar*(150+15/ss+600/sg)

        vastekosten = 3643200

        totaal = materiaal + personeel + vastekosten 
        return totaal

    def klein_robot_5(sg):
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

        vastekosten = 1375000*((0.5+0.9/ss+24/sg*317)/8760)+3187800

        totaal = materiaal + personeel + vastekosten 
        return totaal

    def groot_robot_4(sg):
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

        vastekosten = 1200000*((0.5+0.9/ss+24/sg*159)/8760)+3187800

        totaal = materiaal + personeel + vastekosten 
        return totaal

    def klein_robot_4(sg):
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

        vastekosten = 1100000*((0.5+0.9/ss+24/sg*317)/8760)+3187800

        totaal = materiaal + personeel + vastekosten 
        return totaal

    def groot_robot_5(sg):
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

        vastekosten = 1500000*((0.5+0.9/ss+24/sg*159)/8760)+3187800

        totaal = materiaal + personeel + vastekosten 
        return totaal


def plot(self,titel):
    figure = plt.figure()
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


def plot_test(self,titel):
    fig, ax = plt.subplots()
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

    ax.legend(handles=[p1, p2, p3])
    fig.savefig("./plaatproductie/"+titel+" 3-in-1.png")

plot(totaal.groot_robot_5,"robot, groot, 5 stations")
plot(totaal.groot_robot_4,"robot, groot, 4 stations")
plot(totaal.klein_robot_5,"robot, klein, 5 stations")
plot(totaal.klein_robot_4,"robot, klein, 4 stations")
plot(totaal.klein_hand,"hand, klein")
plot(totaal.groot_hand,"hand, groot")

plot_test(totaal.groot_robot_5,"robot, groot, 5 stations")
plot_test(totaal.groot_robot_4,"robot, groot, 4 stations")
plot_test(totaal.klein_robot_5,"robot, klein, 5 stations")
plot_test(totaal.klein_robot_4,"robot, klein, 4 stations")
plot_test(totaal.klein_hand,"hand, klein")
plot_test(totaal.groot_hand,"hand, groot")

