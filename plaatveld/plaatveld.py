import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
import math as m

ss_np = np.array(np.arange(300,1001))
sg_np = np.array(np.arange(2000,4001))
l_np = np.array(np.arange(100,400))
sigma = 355
rho = 1025
g = 9.81
l = 12000
b = 12000
p = 8 * rho * g *10**-6
Ks = 1.2
rho2=7800 /    10**9
Cm=1.20
ss, sg = np.meshgrid(np.linspace(300,1000,100), np.linspace(2000,4001,100))

hws_supplier = np.array([70])
sg_supplier = np.array([400])#nog in te vullen

hws_offshoresupply = np.array([130])
sg_offshoresupply = np.array([550])#nog in te vullen

hws_feeder = np.array([150])
sg_feeder = np.array([660])


class maat():
    def tp(afstand1):
        Ks = 1.2 
        tp = ((p*(afstand1)**2*Ks)/(2*sigma))**0.5
        return tp

    def tws(afstand1):
        q=((36-24*2**0.5)*p*afstand1*1.2)/(sigma)
        return q

    def Hws():
        hws = (6**0.5/2+3**0.5/2)*((p*ss*sg**2*1.2)/(12*sigma*maat.tws(ss)))**0.5
        return hws
    def Hws_opt(afstand1,afstand2):
        hws = (6**0.5/2+3**0.5/2)*((p*afstand1*afstand2**2*1.2)/(12*sigma*5))**0.5
        return hws

    def hws():
        vHws= np.vectorize(maat.Hws)
        HWS = vHws()
        return HWS

    def Hws_min():
        hws = (6**0.5/2+3**0.5/2)*((p*ss*sg**2*1.2)/(12*sigma*5))**0.5
        return hws

    def hws_min():
        vHws= np.vectorize(maat.Hws_min)
        HWS = vHws()
        return HWS
    '''((9*druk*afstand*1.2)/((3**0.5/2+6**0.5/2)**2*vloeispanning))'''


    def twg(afstand1):
        q= (6*p*afstand1*1.2)/sigma
        return q

    def hwg(afstand1,afstand2):
        q= ((p*afstand1*afstand2**2 * 1.2)/(8*sigma*maat.twg(afstand1)))**0.5
        return q

    def Awg(afstand1,afstand2):
        q= ((2/3)**0.5-(1/6)**0.5)*((p*afstand1*afstand2**2 * maat.twg(afstand1) * 1.2)/(12*sigma))**0.5
        return q

    def tp_max(afstand1):
        q= ((6*(11*afstand1**2)/270)/(sigma))**0.5
        return q

def tp():        
    figure = plt.figure()
    plt.xlabel("stiffnerspacing [mm]")
    plt.ylabel("plaatdikte [mm]")
    plt.title("plaatdikte als functie van ss met minimale plaatdikte")
    plt.plot(ss_np,maat.tp(ss_np), label="plaatdikte")
    plt.axhline(5,c="orange",label="minimaal")
    plt.legend(loc = "lower right", shadow = True, fontsize="large")
    plt.show()
    figure.savefig("plot 1.png")

def tws():       
    figure = plt.figure()
    plt.xlabel("stiffnerspacing [mm]")
    plt.ylabel("webdikte [mm]")
    plt.title("webdikte als functie van stiffnerspacing met minimale webdikte")
    plt.plot(ss_np,maat.tws(ss_np), label="webdikte")
    #plt.axhline(5,c="orange",label="minimaal")
    plt.legend(loc = "lower right", shadow = True, fontsize="large")
    plt.show()
    figure.savefig("plot 2.5.png")

def twg():        
    figure = plt.figure()
    plt.xlabel("girderspacing [mm]")
    plt.ylabel("webdikte [mm]")
    plt.title("webdikte als functie van girderspacing met minimale webdikte")
    plt.plot(sg_np,maat.twg(sg_np), label="webdikte")
    #plt.axhline(5,c="orange",label="minimaal")
    plt.legend(loc = "lower right", shadow = True, fontsize="large")
    plt.show()
    figure.savefig("plot 3.5.png")

def hwg():        
    figure = plt.figure()
    plt.xlabel("girderspacing [mm]")
    plt.ylabel("webhoogte [mm]")
    plt.title("webhoogte als functie van sg")
    plt.plot(sg_np,maat.hwg(sg_np), label="webhoogte")
    #plt.axhline(5,c="orange",label="minimaal")
    plt.legend(loc = "lower right", shadow = True, fontsize="large")
    plt.show()
    figure.savefig("plot 4.png")

def afg():        
    figure = plt.figure()
    plt.xlabel("girderspacing [mm]")
    plt.ylabel("flensoppervlakte [mm^2]")
    plt.title("flensopp. als functie van sg")
    plt.plot(sg_np,maat.Awg(sg_np,b), label="plaatdikte")
    #plt.axhline(5,c="orange",label="minimaal")
    plt.legend(loc = "lower right", shadow = True, fontsize="large")
    plt.show()
    figure.savefig("plot 5.png")




#vraaag 1 G
ss_supplier = np.array([300])
tp_supplier = np.array([4])

ss_offshoresupply = np.array([500])
tp_offshoresupply = np.array([8])

ss_feeder = np.array([660])
tp_feeder = np.array([10])
def scatter():
    #1 vraag G
    figure = plt.figure()
    plt.scatter(ss_supplier,tp_supplier, c="green", label = "crew supplier")
    plt.scatter(ss_offshoresupply,tp_offshoresupply, c="orange", label ="offshore supply vessel")
    plt.scatter(ss_feeder,tp_feeder, c="red", label = "container feeder")
    plt.xlabel("stiffner spacing [mm]")
    plt.ylabel("plaatdikte [mm]")
    plt.title("scatter points tanktops van de drie damen schepen")
    plt.legend(loc = "lower right", shadow = True, fontsize="large")
    plt.axhline(8,c="orange",label="minimale plaat")
    plt.plot(ss_np,maat.tp(ss_np))
    plt.show()
    figure.savefig("plot scatter.png")

def plot_3d():
    #2 vraag F
    figure = plt.figure(figsize= (16,9))
    ax = plt.axes(projection="3d")
    surf = ax.plot_surface(ss,sg,maat.hws(), cmap=cm.cool_r)
    ax.set_xlabel("stiffner spacing [mm]")
    ax.set_ylabel("girder spacing [mm]")
    ax.set_zlabel("web hoogte [mm]")
    ax.set_title("webhoogte als functie van stiffnerspacing en girderspacing")
    #figure.colorbar(surf,shrink=0.5,aspect=5)
    #ax.legend(loc = "lower right", shadow = True, fontsize="large")
    plt.show()
    figure.savefig('plot 3d.png')

def plot_3d_min():
    #2 vraag F
    figure = plt.figure(figsize= (16,9))
    ax = plt.axes(projection="3d")
    surf = ax.plot_surface(ss,sg,maat.hws_min(), cmap=cm.cool_r)
    ax.set_xlabel("stiffner spacing [mm]")
    ax.set_ylabel("girder spacing [mm]")
    ax.set_zlabel("web hoogte [mm]")
    ax.set_title("webhoogte als functie van stiffnerspacing en girderspacing")
    #figure.colorbar(surf,shrink=0.5,aspect=5)
    #ax.legend(loc = "lower right", shadow = True, fontsize="large")
    plt.show()
    figure.savefig('plot 3d min.png')

def tp_minimaal():        
    figure = plt.figure()
    plt.xlabel("L [m]")
    plt.ylabel("plaatdikte [mm]")
    plt.title("minimaal vereiste plaatdikte over L")
    plt.plot(l_np,maat.tp_max(l_np), label="plaatdikte")
    plt.axhline(5,c="orange",label="minimaal")
    plt.legend(loc = "lower right", shadow = True, fontsize="large")
    plt.show()
    figure.savefig("plot 6.png")


def CM(Sg,Ss):
    q = Cm*rho2*(b*np.rint((b/Sg)-1)*(maat.twg(Sg)*maat.hwg(Sg,b)+maat.Awg(Sg,b))+Sg*np.rint((l/Ss)-1)*(maat.tws(Ss)*maat.hws())+l*b*8) #maat.tp(ss)
    return q


CMvar = CM(sg,ss)

def plotCM():
    figure = plt.figure(figsize= (16,9))
    ax = plt.axes(projection="3d")
    surf = ax.plot_surface(ss,sg,CMvar, cmap='summer')
    ax.set_xlabel("stiffner spacing [mm]")
    ax.set_ylabel("girder spacing [mm]")
    ax.set_zlabel("kosten [euro]")
    ax.set_title("kosten als functie van stiffnerspacing en girderspacing")
    #figure.colorbar(surf,shrink=0.5,aspect=5)
    #ax.legend(loc = "lower right", shadow = True, fontsize="large")
    plt.show()
    figure.savefig('plot kosten.png')

x = 300
y = 4000

print(
    "tp",maat.tp(x),
    "hws",maat.Hws_opt(x,y),
    "tws",maat.tws(x),
    "hwg",maat.hwg(y,b),
    "twg",maat.twg(y),
    "afg",maat.Awg(y,b),
)

twg()