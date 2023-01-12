#G&S beladen
import math
import numpy as np

#hoek door gewicht
Ld= 9.3
Lr=28
B=14.3
T=1.6
displ= 0.5*Ld*B*T + Lr*B*T
#TPC=
KB= 0.8
#It=
KG= 2.5 #deelsbeladen
#w1=
#kraanh1=
#kraanb1=
#w2=
#kraanh2=
#kraanb2=
rho=1.025


LCF = ((0.5*Ld*B*T)*(Lr+(1/3)*Ld) + (Lr*B*T)*0.5*Lr)/displ
print(LCF)

#zwaartepunten
gewichten = np.array([1,2,3,4])
armen = np.array([1,2,3,4])
#stabiliteitsreductie

rhovloeistof=1.0
Bv= 3
Lv= 3

'''
def hoek():
    dT=((w1+w2)/TPC)/100
    namb1=(displ+w1+w2)/rho
    BM1=It/namb1
    KB1=(KB*rho*displ+(T+(1/2*dT))*(w1+w2))/(rho*displ+w1+w2)
    KG1=(KG*rho*displ+kraanh1*w1+kraanh2*w2)/(rho*displ+w1+w2)
    GM1=KB1+BM1-KG1
    
    G1G2=(w1*kraanb1+w2*kraanb2)/(displ+w1+w2)
    rad=math.atan(G1G2/GM1)
    graden=rad*180/math.pi
    return graden


def zwaartepunt():
    ZP = (np.sum(gewichten*armen))/np.sum(gewichten)
    return ZP


def vrijvloeistof():
    Iv=(Bv**3*Lv)/12
    reductie = (rhovloeistof*Iv)/(rho*displ)
    return reductie
    
print(hoek())
'''
import math as mt
#Assesment Beladen'
#P = 1.025              #RHO
"""Oppervlaktes 
B = 
H =      
#r =    
Rechthoek = B*H
Driekoek = B*H/2  
Cirkel =   mt.pi * r**2
Oppervlakte ellips = mt.pi * a/2 *b/2  #a = korte as en b = lange as
'''Volume = 
L =                     #Lengte
B =                     #Breedte
D =                     #Diepgang
V = L * B * D           #Volume
'''
#V = 
#Depl = P * V           #Deplacement
#Depl = 

'''Drijfvermogen'''
'''
TPC = P . AWP /100      #L = last en AWP = waterlijnOpp
DeltaT = (L/TPC) / 100  #DeltaT = Diepgangsverandering
'''
#Schip stabiel wanneer Krachtevenwicht en momentevenwicht = 0
'''Metacentrische hoogte'''
#kleine hoeken
'''
GZ = GM * sin(Alpha)
MS = GZ * 9.81 * V
It = 
BM = It/V

BM1 = It/(Depl+L/P)
KB1 = (KB * Depl + (T + (DeltaT / 2)) * L) / (w)
KG1 = (KG * Depl + KT * L)/w
GM =  KB + BM - KG
GM1 = KB1 + BM1 - KG1
'''
'''Stabiliteitsreductie (hellingshoek)
GG1 = (Iv/(Depl+Vtank))
GM2 = KB1 + BM1 - KG1 - GG1
Alpha2 = mt.atan(GG/GM1)
'''
'''traagheidsmomenten
Rechthoek  = 1/12 (B * H**3)
Cirkel = 1/4*(mt.pi * r**4 )
Ellips = 1/4*(mt.pi * a * b**3) #a = korte as en b = lange as
Driehoek = 1/36*(b*h**3) #parralel met de as
Driehoek = 1/48*(h*b**3) #door zwaartepunt en top
'''
'''
#zwaartepunten
gewichten = np.array([1,2,3,4])
armen = np.array([1,2,3,4])
def zwaartepunt():
    ZP = (np.sum(gewichten*armen))/np.sum(gewichten)
    return ZP
'''
"""

gm1 = kb1 + It/displ - kg1