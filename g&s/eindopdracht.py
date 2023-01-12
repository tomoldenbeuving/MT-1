#importeren van de benodigde packages 
import numpy as nm
import matplotlib.pyplot as plt
#studienummer
sdnum = [5,6,8,4,7,5,7]

#gegevens vervoersproblematiek
afstand = 4000+1000*sdnum[1] # [nm]
lalo_snelheid = 750 # [t/uur]
prijs_brandstof = 550+(3*sdnum[2]*sdnum[3]) # [euro/t]
opbrengst_per_ton = 125 # [euro/t]

#gegevens van het schip
Lschip = 100+(sdnum[4]*sdnum[5]) # [m]
Bschip = Lschip/7  # [m]
Tschip = Bschip/2.5 # [m]
Cb_schip = 0.65 + (1/100)*(sdnum[6]*sdnum[3]) # [-]
Depl_schip = Lschip* Bschip* Tschip* Cb_schip # [m^3]
Dwt_schip = 0.73*Depl_schip*1.025 # [t]

#snelle array voor verschillende snelheiden
V = nm.array(range(1,26))

#voorafgaande berekeningen
vermogen = 1.38*10**-4 * Depl_schip * V**3 # [kW]
reistijd = afstand/V + 2*(Dwt_schip/lalo_snelheid + 5) # [uur]

def ecomodel(pb,depl,dwt,rt,bp,fr):
    '''ECOMODEL Deze funcite rekent voor 1 vermogen (Pb) en 1 bijbehorende reistijd de kosten (K)
    en opbrengsten (O) per reis voor een schip met deplacement (depl) en laadvermogen (dwt) uit voor een 
    vaste brandstofprijs en freightrate
    ''' 
    Kosten_vast = (10*depl)/(15*8760)*rt # [euro]
    
    Kosten_bunker = pb * 181 * 10**-6 * bp # [euro/uur]
    
    Kosten_variabel = (Kosten_bunker + 0.05*depl)/rt # [euro]
    
    Kosten = Kosten_vast + Kosten_variabel # [euro]
    
    #voor het plotten zodadelijk Opbrengst aangemaakt als array
    O = 25*[dwt*fr] # [euro]

    #plotten van de Kosten en Opbrengst over verschillende snelheden    
    K_O_V = plt.figure()
    plt.xlim(0,25)
    plt.ylim(0,15000)
    plt. plot(V,Kosten,color = "red", label="Kosten" )
    plt.plot (V, O, color="g", label='Opbrengst')
    plt.xlabel("snelheid [kn]")
    plt.ylabel("Opbrengst en Kosten [euro]")
    plt.title("Kosten en Opbrengst op verschillende snelheden")
    plt.legend(loc = "lower right", shadow = True, fontsize="large")
    plt.show()
    
    #plotten van de Winst op verschillende snelheden
    Winst = plt.figure()
    plt.plot(V,O-Kosten,color = "blue", label="Winst" )
    plt.xlabel("snelheid [kn]")
    plt.ylabel("Winst [euro]")
    plt.title("Winst op verschillende snelheden")
    plt.legend(loc = "lower right", shadow = True, fontsize="large")
    plt.show()
    
   
ecomodel(vermogen, Depl_schip, Dwt_schip, reistijd, prijs_brandstof, opbrengst_per_ton)
    
    