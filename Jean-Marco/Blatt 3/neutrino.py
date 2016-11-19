import ROOT
import numpy as np
import matplotlib.pyplot as plt

write_file = ROOT.TFile("NeutrinoMC.root", "RECREATE")
Signal_MC = ROOT.TTree("Signal_MC", "Geile Neutrino Ereignisse!")

fill_me = np.zeros(1, dtype=float)
#fill_me = np.zeros(1)
Signal_MC.Branch('Energie', fill_me, 'Energy/TeV')

zufall = ROOT.TRandom(34123) # Zufallsgenerator mit random seed
gamma = 2.7
Phi_0 = 1

def transform(r):
    return (1 - r )**(1/(1-gamma))

a1 = []
for i in range(10**5):
    tmp = transform(zufall.Rndm())
    a1.append(tmp)
    fill_me[0] = tmp
    Signal_MC.Fill()


plt.hist(a1, bins=range(0,50) ,alpha=0.8)
plt.title(r"Fancy Neutrinosignale")
#plt.plot(aunw, aunw*0+1000, '-r')
plt.savefig('1a.pdf')

plt.clf()

plt.hist(a1, bins=range(0,10),alpha=0.8)
plt.title(r"Fancy Neutrinosignale")
#plt.plot(aunw, aunw*0+1000, '-r')
plt.savefig('1a_2.pdf')

plt.clf()

bin1 = np.linspace(0, 3, 50)
plt.hist(a1, bins=bin1,alpha=0.8)
plt.title(r"Fancy Neutrinosignale")
#plt.plot(aunw, aunw*0+1000, '-r')
plt.savefig('1a_3.pdf')

plt.clf()

bin1 = np.linspace(0, 3, 50)
plt.hist(a1, bins=50,alpha=0.8)
plt.title(r"Fancy Neutrinosignale")
#plt.plot(aunw, aunw*0+1000, '-r')
plt.savefig('1a_4.pdf')

write_file.Write()
write_file.Close()
