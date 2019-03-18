"""
Plot the scattering cross section as a function of wavelength for 1 micron water droplets
"""

import numpy as np
import matplotlib.pyplot as plt
import miepython
import urllib
import segelstein



def mie_scatter (radius, lam,m):
    x = 2*np.pi*radius/lam
    num = len(lam)
    qqsca = np.zeros(num)
    qqext = np.zeros(num)

    for i in range(num) :
        qext, qsca, qback, g = miepython.mie(m[i],x[i])
        qqsca[i]=qsca
        qqext[i]=qext
    
    ssa = qqsca/qqext #single scattering albedo
    
    return qqsca, ssa

#load refractive index of water data
url = 'http://www.philiplaven.com/Segelstein.txt'
lam,rfr,rfi = segelstein.segel(url)
lam = np.array(lam) #microns
rfr = np.array(rfr)
rfi = np.array(rfi)

m = rfr + 1j*rfi 

radius1 = 7.5                     # in microns
radius2 = 2.5                     # in microns
lam1 = lam[np.where(np.logical_and(lam>=0.4, lam <=1.7))] # also in microns
rfr1 = rfr[np.where(np.logical_and(lam >= 0.4, lam <= 1.7))]
rfi1 = rfi[np.where(np.logical_and(lam >= 0.4, lam <= 1.7))]
m1 = rfr1 + 1j*rfi1 

lam2 = lam[np.where(np.logical_and(lam>=10, lam <=30))] # also in microns
rfr2 = rfr[np.where(np.logical_and(lam >= 10, lam <= 30))]
rfi2 = rfi[np.where(np.logical_and(lam >= 10, lam <= 30))]
m2 = rfr2 + 1j*rfi2

qe_a1, ssa_a1 = mie_scatter(radius1, lam1,m1)
qe_a2, ssa_a2 = mie_scatter(radius2, lam1,m1)
qe_b1, ssa_b1 = mie_scatter(radius1, lam2,m2)
qe_b2, ssa_b2 = mie_scatter(radius2, lam2,m2)
   
plt.figure(figsize = (8,6))
plt.plot(lam1*1000,qe_a1,'k--',label='d = 5 micron')
plt.plot(lam1*1000,qe_a2,'r--',label='d = 15 micron')
plt.title(r"Mie scattering efficiency - 2a")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Scattering Efficiency")
#plt.ylim(1,3)
plt.legend()
plt.show()

plt.figure(figsize = (8,6))
plt.plot(lam1*1000,ssa_a1,'k--',label='d = 5 micron')
plt.plot(lam1*1000,ssa_a2,'r--',label='d = 15 micron')
plt.title(r"Single scatterig albedo- 2a")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Single Scattering Albedo")
plt.legend()
#plt.ylim(1,3)
plt.show()

plt.figure(figsize = (8,6))
plt.plot(lam2*1000,qe_b1,'k--',label='d = 5 micron')
plt.plot(lam2*1000,qe_b2,'r--',label='d = 15 micron')
plt.title(r"Mie scattering efficiency - 2b")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Scattering Efficiency")
plt.legend()
#plt.ylim(1,3)
plt.show()

plt.figure(figsize = (8,6))
plt.plot(lam2*1000,ssa_b1,'k--',label='d = 5 micron')
plt.plot(lam2*1000,ssa_b2,'r--',label='d = 15 micron')
plt.title(r"Single scattering albedo- 2b")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Single Scattering Albedo")
plt.legend()
#plt.ylim(1,3)
plt.show()
