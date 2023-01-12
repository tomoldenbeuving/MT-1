import numpy as np
from scipy import integrate 

maten_spanten = np.array([  [0.00  ,0.00,   0.00,   0.00,   0.6],
                	[0.48,	1.47,	1.92,	2.67,	4.13],
                	[2.34,	4.22,	5.11,	5.91,	6.65],
                	[4.354,	6.23,	6.867,	7.35,	7.623],
                	[5.72,	7.65,	7.96,	8.0,	8.0],
                	[6.0,	7.85,	8.0,	8.0,	8.0],
                	[5.22,	7.28,	7.73,	7.87,	7.96],
                	[3.588,	5.688,	6.3,	6.65,	7.0],
                	[1.52,	3.56,	4.28,	4.81,	5.32],
                	[0.23,	1.39,	1.88,	2.28,	2.69],
                    [0.  ,0., 0.  ,0.   ,   0.0]])	

maten_waterlijnen = np.rot90(maten_spanten)			


hoogtes = np.array([5.00,3.75,2.50,1.25,0.00])	
ordinaten= np.array([0.,2.,4.,6.,8.,10.,12.,14.,16.,18.,20.])

Aspant = 2*integrate.simpson(maten_spanten, dx =1.25)

Awaterlijn = 2*integrate.simpson(maten_waterlijnen, dx=7.9)
    
    
volume = integrate.simpson(Aspant, dx= 79/10)

CWL = maten_spanten[0:11,4]
ACWL = 2* (integrate.simpson(CWL, dx= 79/10) + 0.5* 0.6*1.13) 

lijstzwpunten = integrate.simpson(maten_spanten[0:10]**2, dx=1.25)
 

LCF = (2*integrate.simpson(CWL*ordinaten*(7.9/2), dx=7.9))/ACWL

It = (2/3)* integrate.simps((CWL)**3, dx= 7.9) + 0.6*1.13**3*(1/12)


Sspant = integrate.simpson(Aspant*ordinaten*(7.9/2), dx =7.9)

Swaterlijn = integrate.simpson(Awaterlijn*hoogtes , dx=1.25)

LCB = Sspant/volume

KB = Swaterlijn/volume