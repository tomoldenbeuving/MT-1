import numpy as np
import math as m

tps = 12
ss = 630
hws = 180
tws = 8
wfs = 60
tfs = 12

def z(A,zi):
    z= np.sum(A*zi)/np.sum(A)
    return z

#strip
z_strip = np.array([0.5*tps,0.5*hws+tps])
A_strip = np.array([tps*ss,tws*hws])
ztot_strip = z(A_strip,z_strip)
print("z van strip:",ztot_strip )


#bulb
z_bulb = np.array([0.5*tps,109+tps])
A_bulb = np.array([tps*ss,1890])
ztot_bulb = z(A_bulb,z_bulb)
print("z van bulb:", ztot_bulb)

#hoek
z_hoek = np.array([0.5*tps, 0.5*(hws-tfs)+tps, tps+hws-0.5*tfs])
A_hoek = np.array([tps*ss,tws*(hws-tfs),tfs*wfs])
ztot_hoek = z(A_hoek,z_hoek)
print("z van hoek:", ztot_hoek)

#T
z_T = np.array([0.5*tps, 0.5*(hws-tfs)+tps, tps+hws-0.5*tfs])
A_T = np.array([tps*ss,tws*(hws-tfs),tfs*wfs])
print("z van T:",z(A_T,z_T))

#traagheid plaat met groote verstijver
It1 = tps**3*ss/12 + (hws-tfs)**3*tws/12  + tfs**3*wfs/12 
steiner_L_en_T =  np.sum((z_hoek-ztot_hoek)**2*A_hoek)
It_L_en_T = It1 + steiner_L_en_T

print("It hoek en T verstijver: ",int(It_L_en_T))

#traagheid bulb

Iflange = 609000
steiner_bulb = np.sum((z_bulb-ztot_bulb)**2*A_bulb)
It_bulb = Iflange + steiner_bulb

print("It van de bulb:",It_bulb)

#traagheid stripverstijver

It2 = tps**3*ss/12 + (hws)**3*tws/12
steiner_strip = np.sum((z_strip-ztot_strip)**2*A_strip)
It_strip = It2 + steiner_strip

print("It strip:",int(It_strip))



#girder
tpg = 12
sg = 2100
hwg = 400
twg = 10
wfg = 100
tfg = 20

z_girder = np.array([0.5*tpg, 0.5*(hwg-tfg)+tpg, tpg+hwg-0.5*tfg])
A_girder = np.array([tpg*sg,twg*(hwg-tfg),tfg*wfg])
ztot_girder = z(A_girder,z_girder)
print("z van de plaat-girder:",ztot_girder)

It3 = tpg**3*sg/12 + (hwg-tfg)**3*twg/12  + tfg**3*wfg/12 
steiner_girder =  np.sum((z_girder-ztot_girder)**2*A_girder)
It_girder = It3 + steiner_girder

print("It plaat-girder: ",int(It_girder))

print("It van verstijvers gemiddeled:", (It_strip+It_L_en_T+It_bulb)/3)