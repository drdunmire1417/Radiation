"""
Import Segelstein Refractive Index
"""
def segel(url):
    import urllib
    
    # first, read refractive index data from web (see earlier code in class)
    lines  = urllib.request.urlopen(url).readlines()
    
    # Loop over the lines in the file
    lam=[] # wavelengths (micron)
    rfr=[] # real part of refractive index
    rfi=[] # imaginary part of refractive index
    for line in lines[4:]: # skip first few header line
        entries = line.decode("utf-8").split("\t")
        #print(entries)
        if entries[0][0] != '\n':
            lam.append(float(entries[0]))
            rfr.append(float(entries[1]))      
            rfi.append(float(entries[2]))
    return(lam,rfr,rfi)
   
if __name__=='__main__':    
    import matplotlib.pyplot as plt
    import numpy
    url = 'http://www.philiplaven.com/Segelstein.txt'
    lam,rfr,rfi=segel(url)
    plt.plot(lam,rfr,'b',label='Real Part')
    plt.plot(lam,rfi,'r',label='Imaginary Part')
    plt.title('Liquid Water Refractive Index')
    plt.xlim(0.3,0.8)
    plt.yscale('log')
    plt.xlabel('Wavelength [micron]')
    plt.ylabel('n')
    plt.legend()
    
    plt.figure('T')
    lam=np.array(lam)
    rfi=np.array(rfi)
    T=np.exp(-np.pi*4*rfi/(lam*1e-6)*20)
    plt.plot(lam,T)
    plt.xlim(0.3,0.7)
    
    plt.plot([0.430,0.430],[0,1],'b')
    plt.plot([0.540,0.540],[0,1],'g')
    plt.plot([0.580,0.580],[0,1],'r')
    plt.xlabel('Wavelength [micron]')
    plt.ylabel('Transmittance')
    
    b0=np.argmin(np.abs(lam-0.430))
    g0=np.argmin(np.abs(lam-0.540))
    r0=np.argmin(np.abs(lam-0.580))
    
    red=np.zeros([100,100])
    grn=np.zeros([100,100])
    blu=np.zeros([100,100])
    red[...]=T[r0]
    grn[...]=T[g0]
    blu[...]=T[b0]
    img=np.stack([red,grn,blu],axis=2)
    plt.figure('G')
    plt.imshow(img)
    
# A: Put this into Jupyter notebook
# B: Make color "bar" with actual RGB images that I create, then use imshow()    
    
    # 
# Tasks:
# 1) Calculate transmittance from 300-800 nm through swimming pool (2 m) and water droplet (1 mm)
# 2) Calculate Fresnel Reflection @ 500 nm @ normal incidence and as function of angle
    
