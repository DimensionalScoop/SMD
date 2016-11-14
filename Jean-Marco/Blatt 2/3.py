import ROOT
import numpy as np
import matplotlib.pyplot as plt


zufall = ROOT.TRandom(34123) # Zufallsgenerator mit random seed
xmin = 2
xmax = 7
tau = 100
n=4

def transform_a(r):
    return r * (xmax - xmin) + xmin

def transform_b(r):
    return -tau * np.log( 1 - r)

def transform_c(r):
    return ( r * xmax**(1-n) - r * xmin**(1-n) + xmin**(1-n) )**(1/(1-n))

def transform_d(r):
    return np.tan( np.pi * r - np.pi/2 )

def transform_e(bins, n, len):
    """ Returns a certain amount of random numbers fullfilling a given histogram

    Args:
        bins: Borders of the bins
        n: Value of the bin
        len: How many random numbers do you need?
     """
    a5=[]
    randomgen = ROOT.TRandom(34123) # Zufallsgenerator mit random seed
    for i in range(len):
        a5.append( (randomgen.Rndm(), randomgen.Rndm() ))
    n = n/(max(n)) #scale height
    final_verteilung = [] # init final distribution
    for i in a5:
        section = np.argmax(bins > i[0])-1 # welchem Binbereich wird diese Zahl zugeordnet?
        if(i[1] < n[section]):
            final_verteilung.append(i[0])
    return final_verteilung

a1 = []
for i in range(10000):
    a1.append(transform_a(zufall.Rndm()))

aunw = np.linspace(2,7,10)

plt.hist(a1)
plt.title(r"Gleichverteilung 3a - Exemplarisch von $x_{min} = 2$ bis $x_{max} = 7$")
plt.plot(aunw, aunw*0+1000, '-r')
plt.savefig('3a.pdf')

plt.clf()

a2 = []
for i in range(100000):
    a2.append(transform_b(zufall.Rndm()))

plt.hist(a2, bins=100)
plt.title(r"Gleichverteilung 3b - Exemplarisch für $\tau = 100$")
plt.savefig('3b.pdf')

plt.clf()

a3 = []
for i in range(100000):
    a3.append(transform_c(zufall.Rndm()))
plt.hist(a3, bins=80)
plt.title(r"Gleichverteilung 3c - $x_{min} = 2$ bis $x_{max} = 7$ und $n = 4$")
plt.savefig('3c.pdf')

plt.clf()

a4 = []
for i in range(10000):
    a4.append(transform_d(zufall.Rndm()))
plt.hist(a4, bins=range(-30,30) ,alpha=0.8)
plt.title(r"Gleichverteilung 3d")
plt.savefig('3d.pdf')

plt.clf()

data = np.load("empirisches_histogramm.npy")
n, bins, patches = plt.hist(data['bin_mid'], bins=np.linspace(0., 1., 50), weights=data['hist'])
# n = Binhöhe, bins = bingrenzen

plt.savefig('3e_1.pdf')


plt.clf()
plt.hist(transform_e(bins, n, 100000), bins=49)
plt.savefig('3e_2.pdf')
