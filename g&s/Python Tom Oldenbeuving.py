#importeren van de benodigde packages
import math
from scipy import optimize, integrate
from datetime import date
import numpy as nm
import matplotlib.pyplot as plt


# 1 

#studienummer array
stdnum = [5,6,8,4,7,5,7]

s6 = stdnum[5]

s7 = stdnum[6]

#scheepafmetingen
L = 100 + (s6 * s7)
B = 22+s7
T = 8 + s6
Cb = 0.7 + (s7/100)

WV = L * B * T * Cb



# 2

#reassigning van studienummer 3
stdnum[2] = 42
#reassigning van studienummer 5 naar pi
stdnum[4] = math.pi




# 3


print("\n# 3")
x = math.sin(0.5*math.pi) 

if x == 1: #als .sin in radialen is zou de uitkomst van 1/2pi 1 moeten zijn
    print('math.sin is in radialen')
else:  
    print('tja, math.sin is niet in radialen')
    
 
    
 
# 4 

print("\n# 4")
#voor gemaak maken we een array van de 3 wiskundige functies
ding4 = ["wis1: " ,math.sin(math.pi * (2*s7)), #sinus functie met pi
         "wis2: " , abs(12 * 10**s7 - math.exp(s6)), #absolute waarde met wetenschappelijk notatie
         "wis3: " , math.log(s6,math.e)] #logaritme van studienummer

print(str(ding4)) #voor esthetisch waarde geprint in string vorm

# 5
print("\n# 5")
if 2>6 or 6<2 or 6==2 or 6<=2 or 2>=6 or 2!=2 == True: #voor gemak alle operatoren in 1 voorwaarde
    print("true")
else: 
    print('false')
 
    
 
# 6 
studnumvec = nm.array([5,6,8,4,7,5,7]) #1 dimensionale vector met numpy



# 7
print("\n# 7")
print("de som van de vector*3:",sum(studnumvec*3)) #de vector met 3 vermendigvuldigen en sommeren



# 8
print("\n# 8")

A = nm.array([[1,42,7,40],[1,2,3,4],[5,6,7,8]]) 

print("\ngroote van vector A:",A.size) #grootte van vector A bepalen met .size

B = nm.ones([3,4])#matrix maken van alleen maar 1-en

print("vectorB: \n",B) #de ones-matrix B printen



# 9
#matrix van verschillende parameters van 5 schepen
            # L[m]  ,B[m]   ,T[m]   ,Cb     ,Vs[kn]
S = nm.array([[397  ,56     ,15.5   ,0.7    ,24],
              [180  ,24     ,9      ,0.65   ,16],
              [35   ,5      ,2.5    ,0.85   ,9],
              [274  ,32     ,12     ,0.75   ,18],
              [220  ,26     ,10     ,0.55   ,26]])

varvectoren = nm.transpose(S) #flippen zodat elke list in de matrix een lijstje van variabelen wordt

SL = S[:,0] #L[m]

SB = S[:,1] #B[m]

ST = S[:,2] #T[m]

SCb = S[:,3] #Cb

SVs = S[:,4] #Vs[kn]

totdispl = nm.absolute( SL* SB* ST* SCb) #waterverplaatsing van alle schepen bij elkaar

Schip45 = S[3:5,0:3] #submatrix van schepen 4 en 5

# 10
#submatrix van 4 en 5 opslaan in een .txt bestand genaamd sub_afmetingen, waardes gescheiden met een comma
nm.savetxt('sub_afmetingen.txt', Schip45 , fmt = '%6.2f', delimiter=",")



# 11
print("\n# 11")
a = nm.array([1,4,6])

#functie om het gemiddelde van bovenstaande vector te berekenen
#door de som van de waardes te delen door de groote van de vector
def gemiddelde(vector):
    gem = nm.sum(vector)/nm.size(vector)
    return gem

print("gemiddelden van",a, "is:",gemiddelde(a))
    


# 12
print("\n# 12")
#functie f als polynoom van studienummer waardes
def f(x):
    return stdnum[4]*x**3 - stdnum[2]*x**2 - stdnum[1]*x - stdnum[0]

print("het nulpunt op x-as van funcite f is", optimize.fsolve(f,0)) #nulpunten van de polynoom bepalen met .fsolve



# 13
#functie om schepen te labelen op grootte
def shipsize(var):
    if var < 15:
        #onder de 15meter, klein want geen vaarbewijs
        return "small"
    elif 15 < var < 25:
        #tussen 15 en 25meter, medium want geen groot vaarbewijs
        return "medium"
    elif 25 < var < 110:
        #tussen 25 en 110meter, large want wel grootvaabewijs nodig
        return "large"
    elif var > 110:
        #over 110meter, ultra large want bovenmaatszeegaand schip per definitie van het BPR
        return "ultra large"
    


# 14
print("\n# 14")
def ones(var):#functie om 
    getal = [0,1,2,3,4,5,6,7,8,9]#van elke waarde in getal
    hoeveelheid=[0,0,0,0,0,0,0,0,0,0]#te turven hoevaak het voorkomt in een array
    for getal in var:
        for waarde in range(0,9):
            if getal == waarde:
                hoeveelheid[waarde] +=1 #door als er een match is op die plek 
                #de waarde van hoeveelheid met 1 te verhogen
    return hoeveelheid


stdnum2 = [5,7,3,2,6,1,1] #mijn studienummer
stdnum3 = [5,6,8,4,7,5,7] #studienummer van Bart

n = stdnum2+stdnum3 #bij erlkaar opgeteld
print("getal: ",[0,1,2,3,4,5,6,7,8,9] ,"\nzovaak:", 
      ones(n))


#15
print("\n# 15")
boodschap = '' #lege string om te waardes uit het bestand aan toe te voegen
for bestand in range(2030): #2030 bestanden te openenen
    bestand = open(f"C:/Users/tomol/.spyder-py3/geheim_tekst/bestand{bestand:04d}.txt","r")
    tekst = bestand.readlines()[0] #tekst uit het bestand in een variabele stoppen
    boodschap += tekst #en die variabele optellen aan lege string boodschap
    bestand.close() #nooit vergeten bestanden te sluiten 
    
print(boodschap)

#16
#functie om zwaartepunt van rechthoek te bepalen 
def G():
    print("\n# 16")
    print("gemaakt door Tom, vul L en B in van rechthoek en ik bepaal het zwaartepunt. Het is vandaag", date.today())
    L16 = input("Lengte:  ") #waardes invullen 
    B16 = input("Breedte: ") 
    
    if L16 ==0 or B16 ==0: 
        print("ey dat is geen rechthoek met die waardes")#als een van de waardes nul is het natuurlijk geen rechthoek
    else:
        print("zwaartepunt ligt op x=",float(L16)/2,"y=",float(B16)/2)#simpelweg waardes delen door 2 voor het zwaartepunt
    
G()



#17

print("\n# 17")
# maak een vectorx aan met de arange functie van numpy van 0 naar 8
x = nm.arange(0,8,math.pi/50)
y = nm.sin(x)
#hetplotten doen we voor :
# we maken een figuur aan
zin = plt.figure()
#verzni zelf de captions voor de x en y−as en de titel
plt.xlabel("tijd [s]")
plt.ylabel("hoeveelheid zin python [mood]")
plt.title("zin in python")
# een grid toevoegen kan verhelderend werken bij een p l o t
plt.grid()
# nu maken we de plot
plt.plot(x,y, color = "black")
# dit commando slaat de figuur op in de directory waarin je werkt
# (in dit geval dus in de zelf de folder als je notebook )
# nog niet nodig plt.savefig("test.png")

plt.show()

#18  

c1 =500+stdnum[4]*stdnum[2]*stdnum[0] #constante voor de weerstand
V = nm.arange(0, 50 , 0.5)*0.5144 #snelheid van het schp in m/s
R = c1 * (V)**2 #formule voor de weerstand R in Newton

weerstand = plt.figure() #R plotten in een grafiek 
plt.plot(V,R, color = "green", label="weerstand") #over de snelheid



#19
print("# 18 & 19")
plt.xlabel("snelheid [ms^-1]") #label op de x-as
plt.ylabel("weerstand [N]") #label op de y-as
plt.title("Tom Oldenbeuving 5684757") #titel boven de grafiek
plt.legend(loc = "lower right", shadow = True, fontsize="large")
plt.show()#boven: nog even een legenda



#20
plt.savefig("weerstand over snelheid.png") #plot opslaan in een .png bestand



#21
print("\n# 21")
#twee arrays overgenomen uit bestand opgave21.py
a=[0.000,  0.135,  0.271,  0.406,  0.677,  1.218,  1.759,  2.164,  2.434, 2.975,
   3.245,  3.785,  4.595,  5.404,  6.213,  6.752,  7.291,  7.829,  8.367, 8.905,
   9.442,  9.978, 10.515, 11.050, 11.718, 12.384, 12.782, 13.178, 13.442,
  13.638, 13.899, 14.158, 14.416, 14.671, 14.986, 15.298, 15.543, 15.724,
  15.903, 16.078, 16.251, 16.419, 16.638, 16.849, 17.001, 17.148, 17.381,
  17.636, 17.829, 17.951, 18.063, 18.177, 18.277, 18.342, 18.399, 18.447,
  18.486, 18.508, 18.525, 18.539, 18.550, 18.555, 18.550, 18.550, 18.550, 0.000]

b=[9.692,  9.695,  9.698,  9.701,  9.710,  9.730,  9.754,  9.775,  9.790,  9.824,
   9.842,  9.881,  9.944, 10.014, 10.088, 10.141, 10.197, 10.255, 10.316, 10.381,
  10.448, 10.519, 10.594, 10.674, 10.783, 10.906, 10.988, 11.078, 11.143,
  11.194, 11.267, 11.346, 11.432, 11.524, 11.649, 11.786, 11.906, 12.002,
  12.104, 12.211, 12.324, 12.441, 12.607, 12.782, 12.919, 13.062, 13.310,
  13.627, 13.906, 14.109, 14.318, 14.564, 14.816, 15.009, 15.205, 15.403,
  15.603, 15.738, 15.872, 16.008, 16.177, 16.414, 16.617, 19.258, 21.900, 21.900]

aoverb = plt.figure() #plotten van a over b
plt.plot(a,b)
plt.xlim(0,25)
plt.ylim(0,25)#domein en bereik instellen
plt.show()
print("Dit lijk op een: Grootspant")



#22
print("\n# 22")
Agrootspant = integrate.simpson(a[0:65],b[0:65])#simpson integratie van de Grootspant met b als afstand tussen y waardes
print(Agrootspant)



#eindopdracht
print("eindopdracht: \n")
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
    plt.ylim(0,15000)#domein en bereik instellen
    plt. plot(V,Kosten,color = "red", label="Kosten" )
    plt.plot (V, O, color="g", label='Opbrengst')
    plt.xlabel("snelheid [kn]")#label op de x-as
    plt.ylabel("Opbrengst en Kosten [euro]")#label op te y-as
    plt.title("Kosten en Opbrengst op verschillende snelheden")
    #boven: titel voor de grafiek, onder: legenda rechtsonder de grafiek
    plt.legend(loc = "lower right", shadow = True, fontsize="large")
    plt.show()
    
    #plotten van de Winst op verschillende snelheden
    Winst = plt.figure()
    plt.plot(V,O-Kosten,color = "blue", label="Winst" )
    plt.xlabel("snelheid [kn]")#x-as label
    plt.ylabel("Winst [euro]")#y-as label
    plt.title("Winst op verschillende snelheden")#titel voor boven de grafiek
    plt.legend(loc = "lower right", shadow = True, fontsize="large")#legenda
    plt.show()
    
   
ecomodel(vermogen, Depl_schip, Dwt_schip, reistijd, prijs_brandstof, opbrengst_per_ton)