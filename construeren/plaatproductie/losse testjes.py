import matplotlib.pyplot as plt
import numpy as np
import math as m
import scipy

ss = np.arange(0.7,0.71,1)
groepsnummer = 2
station  = 5
uren = 8
n_perstation= 3 #aantal pesonen  
T = 8
Ks = 1.
rho = 1025
g = 9.81
p = T *g *rho
rho_plaat = 7800
sigma_y = 305E6
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
capaciteit = 22500 + 4/3* 17280
tws = 0.005
twg = 0.005


class totaal():

    def klein_hand(sg):
        hspant = (6*0.5/2+300.5/2)*((p*ss*sg*2*Ks)/(12*sigma_y*tws))**0.5 /1000

        Mb = p*sg*bp**2/12
        Fs = p*sg*bp/2


        hvrang = 1.25
        A_bulb = (((30*0.5)/15 ) + ((6*0.5)/12)) *sg * (np.sqrt((p*ss*tws)/(12*sigma_y )))
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

        m_plaat = Lp * Bp * tp*rho_plaat 
        m_z = nzaathout*Lp*75
        m_s = np.int32(nspant)*Lp*A_bulb*rho_plaat
        m_g = np.int32(nvrang)*Bp*75
        m_totaal = m_plaat+m_z+m_s+m_g
        materiaal = aantal_jaar*m_totaal
        

        ndraaien = 2
        Tphechten = nplaat-1
        Tplassen = Llas_plaat/14400
        Tzgslassen = (Llas_vrang_verti/1.2 +(Llas_vrang_hori+Llas_zaathout+Llas_spant)/2)*((7.8*5**2)/2000)/0.35
        Tshechten = 0.5*(nspant)
        Tzghechten = 4*(nvrang+nzaathout)
        Tdraaien = ndraaien*2


        urenpplaat = Tphechten + Tplassen+ Tzgslassen+2*Tshechten+2*Tzghechten+2*Tdraaien
        productieuren = Tphechten + Tplassen+ Tzgslassen/2+Tshechten+Tzghechten+Tdraaien
        personeel = aantal_jaar*50* urenpplaat

        nplek = np.int32((productieuren*aantal_jaar)/2000)
        loods = A*nplek

        vastekosten = 90*loods

        totaal = materiaal + personeel + vastekosten 
        return totaal, materiaal, personeel, vastekosten,productieuren

    def groot_hand(sg):
        hspant = (6*0.5/2+300.5/2)*((p*ss*sg*2*Ks)/(12*sigma_y*tws))**0.5 /1000

        Mb = p*sg*bp**2/12
        Fs = p*sg*bp/2


        hvrang = 1.25
        A_bulb = (((30*0.5)/15 ) + ((6*0.5)/12)) *sg * (np.sqrt((p*ss*tws)/(12*sigma_y )))
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

        m_plaat = 2*Lp * Bp * tp*rho_plaat 
        m_z = nzaathout*2*Lp*75
        m_s = np.int32(nspant)*2*Lp*A_bulb*rho_plaat
        m_g = np.int32(nvrang)*Bp*75
        m_totaal = m_plaat+m_z+m_s+m_g
        materiaal = aantal_jaar*m_totaal

        ndraaien = 2
        Tphechten = nplaat-1
        Tplassen = Llas_plaat/14400
        Tzgslassen = (Llas_vrang_verti/1.2 +(Llas_vrang_hori+Llas_zaathout+Llas_spant)/2)*((7.8*5**2)/2000)/0.35
        Tshechten = 0.5*(nspant)
        Tzghechten = 4*(nvrang+nzaathout)
        Tdraaien = ndraaien*2


        urenpplaat = Tphechten + Tplassen+ Tzgslassen+2*Tshechten+4*Tzghechten+2*Tdraaien
        productieuren = Tphechten + Tplassen+ Tzgslassen/2+Tshechten+Tzghechten+2*Tdraaien
        personeel = aantal_jaar*50* urenpplaat

        nplek = np.int32((productieuren* aantal_jaar)/2000)
        loods = 2*A*nplek

        vastekosten = 90*loods

        totaal = materiaal + personeel + vastekosten 
        return totaal, materiaal, personeel, vastekosten,productieuren

    def klein_robot(sg):
        hspant = (6*0.5/2+300.5/2)*((p*ss*sg*2*Ks)/(12*sigma_y*tws))**0.5

        Mb = p*sg*bp**2/12
        Fs = p*sg*bp/2


        hvrang = 1.25
        A_bulb = (((30*0.5)/15 ) + ((6*0.5)/12)) *sg * (np.sqrt((p*ss*tws)/(12*sigma_y )))
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
        
        m_plaat = Lp * Bp * tp*rho_plaat 
        m_z = nzaathout*Lp*75
        m_s = nspant*Lp*A_bulb*rho_plaat
        m_g = nvrang*Bp*75
        m_totaal = m_plaat+m_z+m_s+m_g
        materiaal = aantal_jaar*m_totaal

        loc4en5 = (((Llas_vrang_verti/1.2 +(Llas_vrang_hori+Llas_zaathout)/2)*(7.8*5**2/2000) )/0.6 +2*(nvrang+nzaathout))/2
        loc3 = (Llas_spant/2)*((7.8*5**2)/2000)/0.6
        urenpplaat = np.zeros(len(ss))
        for i in range(len(urenpplaat)):
            if loc3[i] > loc4en5[i]:
                urenpplaat[i] = loc3[i]
            if loc4en5[i] > loc3[i]:
                urenpplaat[i] = loc4en5[i]
        personeel = aantal_jaar*90*urenpplaat
        loods = 1200
        nplekken = ((urenpplaat*aantal_jaar/3)/8400)
        nplekkenint = np.ceil(nplekken)
        bezettingsgraad = nplekken/nplekkenint*100
        for k in range(len(nplekkenint)):
            if nplekkenint[k]==0:
                nplekkenint[k] =1
        vastekosten = 70*loods +275000*nplekkenint*station
        totaal = materiaal + personeel + vastekosten 
        return totaal, materiaal, personeel, vastekosten,urenpplaat

    def groot_robot(sg):
        hspant = (6*0.5/2+300.5/2)*((p*ss*sg*2*Ks)/(12*sigma_y*tws))**0.5

        Mb = p*sg*bp**2/12
        Fs = p*sg*bp/2


        hvrang = 1.25
        A_bulb = (((30*0.5)/15 ) + ((6*0.5)/12)) *sg * (np.sqrt((p*ss*tws)/(12*sigma_y )))
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

        m_plaat = 2*Lp * Bp * tp*rho_plaat 
        m_z = nzaathout*2*Lp*75
        m_s = nspant*2*Lp*A_bulb*rho_plaat
        m_g = nvrang*Bp*75
        m_totaal = m_plaat+m_z+m_s+m_g
        materiaal = aantal_jaar*m_totaal
        
        loc4en5 = (((Llas_vrang_verti/1.2 +(Llas_vrang_hori+Llas_zaathout)/2)*(7.8*5**2/2000))/0.6 +4*(nvrang+nzaathout))/2
        loc3 = (Llas_spant/2)*((7.8*5**2)/2000)/0.6
        urenpplaat = np.zeros(len(ss))
        for i in range(len(urenpplaat)):
            if loc3[i] > loc4en5[i]:
                urenpplaat[i] = loc3[i]
            if loc4en5[i] > loc3[i]:
                urenpplaat[i] = loc4en5[i]

        personeel = aantal_jaar*90*urenpplaat
        loods = 1200
        nplekken = ((urenpplaat* aantal_jaar/3)/8400)
        nplekkenint = np.ceil(nplekken)
        bezettingsgraad = nplekken/nplekkenint*100
        for k in range(len(nplekkenint)):
            if nplekkenint[k]==0:
                nplekkenint[k] =1
        vastekosten = 70*loods +300000*nplekkenint*station

        totaal = materiaal + personeel + vastekosten 
        return totaal, materiaal, personeel, vastekosten,urenpplaat



k_h_4_tot, k_h_4_mat,k_h_4_per,k_h_4_vast,k_h_man = totaal.klein_hand(4)
g_h_4_tot, g_h_4_mat,g_h_4_per,g_h_4_vast,g_h_man = totaal.groot_hand(4)



k_r_4_tot, k_r_4_mat,k_r_4_per,k_r_4_vast,k_r_man = totaal.klein_robot(4)
g_r_4_tot, g_r_4_mat,g_r_4_per,g_r_4_vast,g_r_man = totaal.groot_robot(4)


print([["scenario","manuren"],
       ["hand klein",k_h_man],
       ["hand groot",g_h_man],
       ["robot klein",k_r_man],
       ["robot groot",g_r_man]])

print([["scenario","totaal","materiaal","personeel","vast"],
       ["klein hand",k_h_4_tot, k_h_4_mat,k_h_4_per,k_h_4_vast],
       ["groot hand",g_h_4_tot, g_h_4_mat,g_h_4_per,g_h_4_vast],
       ["klein robot",k_r_4_tot, k_r_4_mat,k_r_4_per,k_r_4_vast],
       ["groot robot",k_r_4_tot, k_r_4_mat,k_r_4_per,k_r_4_vast]])


def bar_plot():
    materiaal_tup = (min(g_h_4_mat),min(g_h_4_mat),min(g_h_4_mat),min(g_h_4_mat))
    personeel_tup = (min(k_h_4_per),min(g_h_4_per),min(k_r_4_per),min(g_r_4_per))
    vastekosten_tup = (min(k_h_4_vast),min(g_h_4_vast),min(k_r_4_vast),min(g_r_4_vast))
    figure = plt.figure(figsize=(10,8))
    ind = np.arange(4)
    plt.bar(ind, np.array(materiaal_tup), 0.35,    color="red", label="materiaal")
    plt.bar(ind, np.array(personeel_tup),  0.35,   bottom=np.array(materiaal_tup),   color="green", label="personeel")
    plt.bar(ind, np.array(vastekosten_tup), 0.35,  bottom=np.array(personeel_tup)+np.array(materiaal_tup),    color="blue", label="vastekosten")
    plt.xticks(ind,["klein, hand","groot, hand","klein, robot","groot, robot"])
    plt.ticklabel_format(style='sci', axis='y', scilimits=(6,6))
    plt.ylabel("kosten [euro]")
    titeltje= "Kosten in de vier scenarios"
    plt.title(titeltje)
    plt.legend(loc = "best", shadow = True, fontsize="small")
    plt.grid()
    figure.savefig("./construeren/plaatproductie/barplot.png")


bar_plot()