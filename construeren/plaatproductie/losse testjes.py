import matplotlib.pyplot as plt
import numpy as np
import math as m
import scipy

ss = np.linspace(0.3,1.0,701)
groepsnummer = 2
station  = 5
uren = 8
n_perstation= 3 #aantal pesonen  
T = 8
Ks = 1.2
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


        hvrang = np.sqrt(3/2)*np.sqrt(Mb * 1.2/(sigma_y*twg))
        A_bulb = 0.40824829 * np.sqrt(Mb*twg*1.2/(sigma_y))
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
        
        x = nplaat-1 + 2
        y = Llas_plaat/14400
        z1 = (Llas_vrang_verti/1.2 +(Llas_vrang_hori+Llas_zaathout+Llas_spant)/2)
        z2 = ((7.8*5**2)/2000)
        z = 1/0.35*(z1*z2)
        x1 = (nspant)
        y1 = 4*(nvrang+nzaathout)


        urenpplaat = x + y + z +x1+ y1
        personeel = aantal_jaar*50* urenpplaat

        nplek = np.int32((urenpplaat*aantal_jaar)/2000)
        loods = A*nplek

        vastekosten = 90*loods

        totaal = materiaal + personeel + vastekosten 
        return min(urenpplaat)

    def groot_hand(sg):
        hspant = (6*0.5/2+300.5/2)*((p*ss*sg*2*Ks)/(12*sigma_y*tws))**0.5 /1000

        Mb = p*sg*bp**2/12
        Fs = p*sg*bp/2


        hvrang = np.sqrt(3/2)*np.sqrt(Mb * 1.2/(sigma_y*twg))
        A_bulb = 0.40824829 * np.sqrt(Mb*twg*1.2/(sigma_y))
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

        urenpplaat = nplaat-1 + 2 + Llas_plaat/14400 + 1/0.35*((Llas_vrang_verti/1.2 +(Llas_vrang_hori+Llas_zaathout+Llas_spant)/2)*(7.8*5**2/2000) )+(nspant)+8*(nvrang+nzaathout)

        personeel = aantal_jaar*50*urenpplaat

        nplek = np.int32((urenpplaat*aantal_jaar)/2000)
        loods = 2*A*nplek

        vastekosten = 90*loods

        totaal = materiaal + personeel + vastekosten 
        return min(urenpplaat)

    def klein_robot(sg):
        hspant = (6*0.5/2+300.5/2)*((p*ss*sg*2*Ks)/(12*sigma_y*tws))**0.5

        Mb = p*sg*bp**2/12
        Fs = p*sg*bp/2


        hvrang = np.sqrt(3/2)*np.sqrt(Mb * 1.2/(sigma_y*twg))
        A_bulb = 0.40824829 * np.sqrt(Mb*twg*1.2/(sigma_y))
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

        urenpplaat = 5*((Llas_vrang_verti/1.2 +(Llas_vrang_hori+Llas_zaathout+Llas_spant)/2)*(7.8*5**2/2000) )/4 +2*(nvrang+nzaathout)
        personeel = aantal_jaar*90*urenpplaat
        loods = 1500
        vastekosten = 70*loods +275000*10*ss/ss
        totaal = materiaal + personeel + vastekosten 
        return min(urenpplaat)
    
    def groot_robot(sg):
        hspant = (6*0.5/2+300.5/2)*((p*ss*sg*2*Ks)/(12*sigma_y*tws))**0.5

        Mb = p*sg*bp**2/12
        Fs = p*sg*bp/2


        hvrang = np.sqrt(3/2)*np.sqrt(Mb * 1.2/(sigma_y*twg))
        A_bulb = 0.40824829 * np.sqrt(Mb*twg*1.2/(sigma_y))
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
        
        urenpplaat = 5*((Llas_vrang_verti/1.2 +(Llas_vrang_hori+Llas_zaathout+Llas_spant)/2)*(7.8*5**2/2000) )/4 +4*(nvrang+nzaathout)
        personeel = aantal_jaar*90*urenpplaat
        loods = 1500
        vastekosten = 70*loods +300000*10*ss/ss

        totaal = materiaal + personeel + vastekosten 
        return min(urenpplaat)

'''
k_h_4_tot, k_h_4_mat,k_h_4_per,k_h_4_vast = totaal.klein_hand(4)
g_h_4_tot, g_h_4_mat,g_h_4_per,g_h_4_vast = totaal.groot_hand(4)

k_h_3_tot, k_h_3_mat,k_h_3_per,k_h_3_vast = totaal.klein_hand(3)
g_h_3_tot, g_h_3_mat,g_h_3_per,g_h_3_vast = totaal.groot_hand(3)

k_h_2_tot, k_h_2_mat,k_h_2_per,k_h_2_vast = totaal.klein_hand(2)
g_h_2_tot, g_h_2_mat,g_h_2_per,g_h_2_vast = totaal.groot_hand(2)

k_r_4_tot, k_r_4_mat,k_r_4_per,k_r_4_vast = totaal.klein_robot(4)
g_r_4_tot, g_r_4_mat,g_r_4_per,g_r_4_vast = totaal.groot_robot(4)

k_r_3_tot, k_r_3_mat,k_r_3_per,k_r_3_vast = totaal.klein_robot(3)
g_r_3_tot, g_r_3_mat,g_r_3_per,g_r_3_vast = totaal.groot_robot(3)

k_r_2_tot, k_r_2_mat,k_r_2_per,k_r_2_vast = totaal.klein_robot(2)
g_r_2_tot, g_r_2_mat,g_r_2_per,g_r_2_vast = totaal.groot_robot(2)
'''

label = ["klein, hand","groot, hand","klein, robot","groot, robot"]
min_uren = [totaal.klein_hand(4),totaal.groot_hand(4),totaal.klein_robot(4),totaal.groot_robot(4)]

tabel = np.array([label,min_uren])

print(tabel)