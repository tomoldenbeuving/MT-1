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
tpmm = 8
Bp = 12
bp = 3
Lp= 12
A= 144
hvrang = 1.25
hspant = 0.16
capaciteit = 22500 + 4/3* 17280

loods = 1730

'''#hand
personeel = 50/0.35(nplaat + 4 + Llas_plaat/15 +(Llas_vrang_verti/1.2 +(Llas_vrang_hori+Llas_zaathout)/2)*(7.8*tp**2/200) 1/2*(nspant)+2*(nvrang+nzaathout))
#robot
personeel = 90/0.60(nplaat + 4 + Llas_plaat/30 +(Llas_vrang_verti/2.4 +(Llas_vrang_hori+Llas_zaathout)/4)*(7.8*tp**2/200) 1/2*(nspant)+2*(nvrang+nzaathout))
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

        urenpplaat = nplaat + 2 + 1/0.35*(Llas_plaat/15 +(Llas_vrang_verti/1.2 +(Llas_vrang_hori+Llas_zaathout+Llas_spant)/2)*(7.8*tpmm**2/2000) )+0.5*(nspant)+4*(nvrang+nzaathout)
        personeel = aantal_jaar*50* urenpplaat

        vastekosten = 90*loods

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

        urenpplaat = nplaat + 2 + 1/0.35*(Llas_plaat/15 +(Llas_vrang_verti/1.2 +(Llas_vrang_hori+Llas_zaathout+Llas_spant)/2)*(7.8*tpmm**2/2000) )+0.5*(nspant)+8*(nvrang+nzaathout)

        personeel = aantal_jaar*50*urenpplaat

        vastekosten = 90*loods

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

        urenpplaat = 1/0.6*(((Llas_zaathout/2+Llas_vrang_verti/1.2+Llas_vrang_hori/2)*7.8*tpmm**2)/4000) +2*(nvrang+nzaathout)
        personeel = aantal_jaar*90*3/5*urenpplaat
        loods = 1500
        vastekosten = 70*loods +275000*10
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

        urenpplaat = 1/0.6*(((Llas_zaathout/2+Llas_vrang_verti/1.2+Llas_vrang_hori/2)*7.8*tpmm**2)/4000) +4*(nvrang+nzaathout)
        personeel = aantal_jaar*90*3/5*urenpplaat
        loods = 1500
        vastekosten = 70*loods +300000*10

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

        materiaal = 35521200*tp + 3415500/sg + 355212000*A_bulb/ss-118404000*A_bulb+1138500+3900*tp*Llas

        personeel = aantal_jaar*(3140+25*nspant+100*nvrang)

        vastekosten = 151773.33

        totaal = materiaal + personeel + vastekosten 
        return materiaal

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

        personeel = aantal_jaar*(3295+25*nspant+200*nvrang)

        vastekosten = 151773.33

        totaal = materiaal + personeel + vastekosten 
        return materiaal

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

        personeel = aantal_jaar*(3933+27*nspant+180*nvrang)

        vastekosten = 106260+229166.67*((43.7+0.3*nspant+2*nvrang)*137/8400)

        totaal = materiaal + personeel + vastekosten 
        return materiaal

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

        personeel = aantal_jaar*(7965+27*nspant+4320*260*nvrang)

        vastekosten = 106260+250000*((88.5+0.3*nspant+4*nvrang)*159/8400)

        totaal = materiaal + personeel + vastekosten 
        return materiaal

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

        materiaal = aantal_jaar*4*(Lp*Bp*7800*tp+Bp*75*Lp/sg+(Bp/ss-1)*Lp*A_bulb*7800+Lp*75)+0.5*7800*tp*Llas

        urenpplaat = nplaat + 2 + 1/0.35*(Llas_plaat/15 +(Llas_vrang_verti/1.2 +(Llas_vrang_hori+Llas_zaathout+Llas_spant)/2)*(7.8*tpmm**2/2000) )+0.5*(nspant)+4*(nvrang+nzaathout)
        personeel = aantal_jaar*50* urenpplaat

        vastekosten = 151773.33

        totaal = materiaal + personeel + vastekosten 
        return personeel

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

        materiaal = aantal_jaar*8*(Lp*Bp*7800*tp+Bp*75*Lp/sg+(Bp/ss-1)*Lp*A_bulb*7800+Lp*75)+0.5*7800*tp*Llas

        urenpplaat = nplaat + 2 + 1/0.35*(Llas_plaat/15 +(Llas_vrang_verti/1.2 +(Llas_vrang_hori+Llas_zaathout+Llas_spant)/2)*(7.8*tpmm**2/2000) )+0.5*(nspant)+8*(nvrang+nzaathout)

        personeel = aantal_jaar*50*urenpplaat

        vastekosten = 151773.33

        totaal = materiaal + personeel + vastekosten 
        return personeel

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

        materiaal = aantal_jaar*4*(Lp*Bp*7800*tp+Bp*75*Lp/sg+(Bp/ss-1)*Lp*A_bulb*7800+Lp*75)+0.5*7800*tp*Llas

        urenpplaat = 1/0.6*(((Llas_zaathout/2+Llas_vrang_verti/1.2+Llas_vrang_hori/2)*7.8*tpmm**2)/4000) +2*(nvrang+nzaathout)
        personeel = aantal_jaar*90*3/5*urenpplaat

        vastekosten = 106260+229166.67*((43.7+0.3*nspant+2*nvrang)*137/8400)

        totaal = materiaal + personeel + vastekosten 
        return personeel

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

        materiaal = aantal_jaar*8*(Lp*Bp*7800*tp+Bp*75*Lp/sg+(Bp/ss-1)*Lp*A_bulb*7800+Lp*75)+0.5*7800*tp*Llas

        urenpplaat = 1/0.6*(((Llas_zaathout/2+Llas_vrang_verti/1.2+Llas_vrang_hori/2)*7.8*tpmm**2)/4000) +4*(nvrang+nzaathout)
        personeel = aantal_jaar*90*3/5*urenpplaat

        vastekosten = 106260+250000*((88.5+0.3*nspant+4*nvrang)*159/8400)

        totaal = materiaal + personeel + vastekosten 
        return personeel

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

        materiaal = 4*(Lp*Bp*7800*tp+Bp*75*Lp/sg+(Bp/ss-1)*Lp*A_bulb*7800+Lp*75)+0.5*7800*tp*Llas

        personeel = aantal_jaar*(3140+25*nspant+100*nvrang)

        vastekosten = 90*loods *ss/ss

        totaal = materiaal + personeel + vastekosten 
        return vastekosten

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

        materiaal = 8*(Lp*Bp*7800*tp+Bp*75*Lp/sg+(Bp/ss-1)*Lp*A_bulb*7800+Lp*75)+0.5*7800*tp*Llas

        personeel = aantal_jaar*(3295+25*nspant+200*nvrang)

        vastekosten = 90*loods  *ss/ss

        totaal = materiaal + personeel + vastekosten 
        return vastekosten

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

        materiaal = 4*(Lp*Bp*7800*tp+Bp*75*Lp/sg+(Bp/ss-1)*Lp*A_bulb*7800+Lp*75)+0.5*7800*tp*Llas

        personeel = aantal_jaar*(3933+27*nspant+180*nvrang)
        loods = 1500
        vastekosten = 70*loods +275000*10 *ss/ss

        totaal = materiaal + personeel + vastekosten 
        return vastekosten

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

        materiaal = 8*(Lp*Bp*7800*tp+Bp*75*Lp/sg+(Bp/ss-1)*Lp*A_bulb*7800+Lp*75)+0.5*7800*tp*Llas

        personeel = aantal_jaar*(7965+27*nspant+4320*260*nvrang)
        loods = 1500
        vastekosten = 70*loods +300000*10  *ss/ss

        totaal = materiaal + personeel + vastekosten 
        return vastekosten



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
    materiaal_tup = (min(materiaal.klein_hand(4)),min(materiaal.groot_hand(4)),min(materiaal.klein_robot(4)),min(materiaal.groot_robot(4)))
    personeel_tup = (min(personeel.klein_hand(4)),min(personeel.groot_hand(4)),min(personeel.klein_robot(4)),min(personeel.groot_robot(4)))
    vastekosten_tup = (min(vastekosten.klein_hand(4)),min(vastekosten.groot_hand(4)),min(vastekosten.klein_robot(4)),min(vastekosten.groot_robot(4)))
    figure = plt.figure(figsize=(10,8))
    ind = np.arange(4)
    plt.bar(ind, np.array(materiaal_tup), 0.35,    color="red", label="materiaal")
    plt.bar(ind, np.array(personeel_tup),  0.35,   bottom=np.array(materiaal_tup),   color="green", label="personeel")
    plt.bar(ind, np.array(vastekosten_tup), 0.35,  bottom=np.array(personeel_tup)+np.array(materiaal_tup),    color="blue", label="vastekosten")
    plt.ylim(2E6,min(totaal.klein_hand(2)))
    plt.xticks(ind,["klein, hand","groot, hand","klein, robot","groot, robot"])
    plt.ylabel("kosten [euro]")
    titeltje= "Minimale Kosten in de vier scenarios"
    plt.title(titeltje)
    plt.legend(loc = "best", shadow = True, fontsize="small")
    figure.savefig("./plaatproductie/barplot.png")



plot(totaal.klein_robot, totaal.groot_robot,"totale kosten robot")
plot(totaal.klein_hand, totaal.groot_hand,"totale kosten hand")


plot(materiaal.klein_robot, materiaal.groot_robot,"materiaal kosten ")

plot(vastekosten.klein_robot, vastekosten.groot_robot,"vastekosten robot")
plot(vastekosten.klein_hand, vastekosten.groot_hand,"vastekosten hand")


plot(personeel.klein_robot, personeel.groot_robot,"personeels kosten robot")
plot(personeel.klein_hand, personeel.groot_hand,"personeels kosten hand")

bar_plot()