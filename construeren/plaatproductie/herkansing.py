import matplotlib.pyplot as plt
import numpy as np
import math as m

ss = np.linspace(0.3,1.0,num=500)
groepsnummer = 2
station  = 5
uren = 8
A_bulb = 0.001780
n_perstation= 3 #aantal pesonen  
T = 8
Ks = 1.2
rho = 1025
g = 9.81
p = T *g *rho
sigma_y = 355E6
tp_form = ss*np.sqrt((p*Ks)/(2*sigma_y))
tp = np.zeros(len(tp_form))

for i in range(len(tp_form)):
    if tp_form[i] <= 0.008:
        tp[i] = 0.008
    else:
        tp[i] = tp_form[i]


tpmm = tp*1000
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
        Llas_spant = nspant*Lp*2  
        Llas_vrang_hori = nvrang*Bp*2  
        Llas_zaathout = nzaathout*Lp*2   
        Llas_vrang_verti = hvrang*nkruising*4 +nspant*hspant*2
        Llas = Llas_plaat + Llas_spant + Llas_vrang_hori + Llas_zaathout + Llas_vrang_verti

        materiaal = 35521200*tp + 3415500/sg + 355212000*A_bulb/ss-118404000*A_bulb+1138500+3900*tp*Llas

        urenpplaat = nplaat + 2 + 1/0.35*(Llas_plaat/15 +(Llas_vrang_verti/1.2 +(Llas_vrang_hori+Llas_zaathout+Llas_spant)/2)*(7.8*tpmm**2/2000) )+0.5*(nspant)+4*(nvrang+nzaathout)
        personeel = aantal_jaar*50* urenpplaat

        nplek = np.int32((urenpplaat*aantal_jaar)/2000)
        loods = A*nplek

        vastekosten = 90*loods

        totaal = materiaal + personeel + vastekosten 
        return totaal, materiaal, personeel, vastekosten

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

        nplek = np.int32((urenpplaat*aantal_jaar)/2000)
        loods = 2*A*nplek

        vastekosten = 90*loods

        totaal = materiaal + personeel + vastekosten 
        return totaal, materiaal, personeel, vastekosten

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
        return totaal, materiaal, personeel, vastekosten

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
        return totaal, materiaal, personeel, vastekosten


k_h_4_tot, k_h_4_mat,k_h_4_per,k_h_4_vast = totaal.klein_hand(4)
g_h_4_tot, g_h_4_mat,g_h_4_per,g_h_4_vast = totaal.groot_hand(4)

k_h_3_tot, k_h_3_mat,k_h_3_per,k_h_3_vast = totaal.klein_hand(3)
g_h_3_tot, g_h_3_mat,g_h_3_per,g_h_3_vast = totaal.groot_hand(3)

k_h_2_tot, k_h_2_mat,k_h_2_per,k_h_2_vast = totaal.klein_hand(2)
g_h_2_tot, g_h_2_mat,g_h_2_per,g_h_2_vast = totaal.groot_hand(2)

def plot_totaal(titel):
    figure = plt.figure(figsize=(12,8))
    plt.plot(ss,k_h_4_tot, c="green"     ,label="$kleine-plaat \quad s_g = 4m$")
    plt.plot(ss,g_h_4_tot, c="darkgreen"     ,label="$grote-plaat \quad s_g = 4m$")
    plt.plot(ss,k_h_3_tot, c="red"     ,label="$kleine-plaat \quad s_g = 3m$")
    plt.plot(ss,g_h_3_tot, c="orange"     ,label="$grote-plaat \quad s_g = 3m$")
    plt.plot(ss,k_h_2_tot, c="blue"     ,label="$kleine-plaat \quad s_g = 2m$")
    plt.plot(ss,g_h_2_tot, c="darkblue"     ,label="$grote-plaat \quad s_g = 2m$")
    plt.xlabel("verstijver spacing [m]")
    plt.ylabel("kosten [euro]")
    titeltje= "Functie van verstijver spacing, voor "+titel
    plt.title(titeltje)
    plt.legend(loc = "best", shadow = True, fontsize="small")
    figure.savefig("./construeren/plaatproductie/"+titel+".png")

def plot_vastekosten(titel):
    figure = plt.figure(figsize=(12,8))
    plt.plot(ss,k_h_4_vast, c="green"     ,label="$kleine-plaat \quad s_g = 4m$")
    plt.plot(ss,g_h_4_vast, c="darkgreen"     ,label="$grote-plaat \quad s_g = 4m$")
    plt.plot(ss,k_h_3_vast, c="red"     ,label="$kleine-plaat \quad s_g = 3m$")
    plt.plot(ss,g_h_3_vast, c="orange"     ,label="$grote-plaat \quad s_g = 3m$")
    plt.plot(ss,k_h_2_vast, c="blue"     ,label="$kleine-plaat \quad s_g = 2m$")
    plt.plot(ss,g_h_2_vast, c="darkblue"     ,label="$grote-plaat \quad s_g = 2m$")
    plt.xlabel("verstijver spacing [m]")
    plt.ylabel("kosten [euro]")
    titeltje= "Functie van verstijver spacing, voor "+titel
    plt.title(titeltje)
    plt.legend(loc = "best", shadow = True, fontsize="small")
    figure.savefig("./construeren/plaatproductie/"+titel+".png")

def plot_personeel(titel):
    figure = plt.figure(figsize=(12,8))
    plt.plot(ss,k_h_4_per, c="green"     ,label="$kleine-plaat \quad s_g = 4m$")
    plt.plot(ss,g_h_4_per, c="darkgreen"     ,label="$grote-plaat \quad s_g = 4m$")
    plt.plot(ss,k_h_3_per, c="red"     ,label="$kleine-plaat \quad s_g = 3m$")
    plt.plot(ss,g_h_3_per, c="orange"     ,label="$grote-plaat \quad s_g = 3m$")
    plt.plot(ss,k_h_2_per, c="blue"     ,label="$kleine-plaat \quad s_g = 2m$")
    plt.plot(ss,g_h_2_per, c="darkblue"     ,label="$grote-plaat \quad s_g = 2m$")
    plt.xlabel("verstijver spacing [m]")
    plt.ylabel("kosten [euro]")
    titeltje= "Functie van verstijver spacing, voor "+titel
    plt.title(titeltje)
    plt.legend(loc = "best", shadow = True, fontsize="small")
    figure.savefig("./construeren/plaatproductie/"+titel+".png")

def plot_materiaal(titel):
    figure = plt.figure(figsize=(12,8))
    plt.plot(ss,k_h_4_mat, c="green"     ,label="$kleine-plaat \quad s_g = 4m$")
    plt.plot(ss,g_h_4_mat, c="darkgreen"     ,label="$grote-plaat \quad s_g = 4m$")
    plt.plot(ss,k_h_3_mat, c="red"     ,label="$kleine-plaat \quad s_g = 3m$")
    plt.plot(ss,g_h_3_mat, c="orange"     ,label="$grote-plaat \quad s_g = 3m$")
    plt.plot(ss,k_h_2_mat, c="blue"     ,label="$kleine-plaat \quad s_g = 2m$")
    plt.plot(ss,g_h_2_mat, c="darkblue"     ,label="$grote-plaat \quad s_g = 2m$")
    plt.xlabel("verstijver spacing [m]")
    plt.ylabel("kosten [euro]")
    titeltje= "Functie van verstijver spacing, voor "+titel
    plt.title(titeltje)
    plt.legend(loc = "best", shadow = True, fontsize="small")
    figure.savefig("./construeren/plaatproductie/"+titel+".png")


plot_vastekosten("vastekosten hand")

plot_totaal("totale kosten hand")

plot_personeel("personeelskosten hand")

plot_materiaal("materiaal kosten")