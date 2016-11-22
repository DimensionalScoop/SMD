import ROOT
import numpy as np
import matplotlib.pyplot as plt
import sys

#Prepare Stuff
write_file = ROOT.TFile("NeutrinoMC.root", "RECREATE")

zufall = ROOT.TRandom(34123) # Zufallsgenerator mit random seed
gamma = 2.7
Phi_0 = 1

#Funktionen für die Aufgabe, Yaay!
def transform(r):
    return (1 - r )**(1/(1-gamma))

def det_p(E):
    '''Returns probabilty of detection for a given E'''
    return (1 - np.exp(-E/2))**3

class Polar_Normal:
    '''Returns standard normal random numbers'''
    def __init__(self,seed):
        self.__zufall = ROOT.TRandom(seed)

    def random_normal(self, mean, sigma):
        '''Returns 2 normal random numbers with sigma and mean'''
        u1 = self.__zufall.Rndm()
        u2 = self.__zufall.Rndm()
        v1 = 2 * u1 - 1
        v2 = 2 * u2 - 1
        s = v1**2 + v2**2
        if s >= 1:
            return self.random_normal(mean, sigma)
        x1 = v1 * np.sqrt( -2/s * np.log(s) )
        x2 = v2 * np.sqrt(- 2/s * np.log(s) )
        return_val = [sigma * x1 + mean, sigma * x2 + mean]
        return return_val

def sigma_ort(N):
    '''Retruns the standard deviation for a given Hit-number N'''
    return 1/np.log10(N+1)

# Aufgabe a
Signal_MC = ROOT.TTree("Signal_MC", "Geile Neutrino Ereignisse!")
fill_me = np.zeros(1, dtype=float)
Signal_MC.Branch('Energie', fill_me, 'Energy/D')

a1 = []
for i in range(10**5):
    tmp = transform(zufall.Rndm())
    a1.append(tmp)
    fill_me[0] = transform(zufall.Rndm())
    Signal_MC.Fill()

plt.hist(np.log(a1), bins=50 ,alpha=0.8)
plt.title(r"Fancy Neutrinosignale")
plt.yscale('log')
#plt.xscale('log')
plt.xlabel(r'$log(E) \,/\, \mathrm{TeV}$')
plt.savefig('fig/1a.pdf')
plt.clf()



# Aufgabe b

Signal_MC_Akzeptanz = ROOT.TTree("Signal_MC_Akzeptanz", "Geile Neutrino Ereignisse mit Detektorempfindlichkeit!")
fill_me2 = np.zeros(1, dtype=float)
Signal_MC_Akzeptanz.Branch('Energie', fill_me2, 'Energy/D')


a2 = [] #Enthält akzeptierte
for i in a1:
    tmp = zufall.Rndm()
    if tmp < det_p(i):
        a2.append(i)
        fill_me2[0] = i
        Signal_MC_Akzeptanz.Fill()

plt.hist(np.log(a2), bins=50 ,alpha=0.8)
plt.title(r"Fancy Neutrinosignale mit Detektorempfindlichkeit")
plt.yscale('log')
#plt.xscale('log')
plt.xlabel(r'$log(E) \,/\, \mathrm{TeV}$')
plt.savefig('fig/1b.pdf')
plt.clf()

plt.hist(np.log(a2), bins=50 ,alpha=0.8, label=r"Akzeptierte Hits")
plt.hist(np.log(a1), bins=50 ,alpha=0.5, label=r"Ursprüngliche Hits")
plt.title(r"Fancy Neutrinosignale mit Detektorempfindlichkeit")
plt.legend(loc='best')
plt.yscale('log')
#plt.xscale('log')
plt.xlabel(r'$log(E) \,/\, \mathrm{TeV}$')
plt.savefig('fig/1b2.pdf')


plt.clf()



# Aufgabe c)

fill_me3 = np.zeros(1, dtype=int) # Würde hier gerne int machen, aber Root scheint den Datentyp int nicht zu verstehen (?)
Signal_MC_Akzeptanz.Branch('AnzahlHits', fill_me3, 'Hits/I')

polargen = Polar_Normal(71231)
a3 = []
for i in a2:
    tmp = 0
    while tmp == 0:
        tmp = polargen.random_normal(10*i, 2*i)
        tmp = np.round(tmp[0]).astype(int)
    a3.append(tmp)
    fill_me3[0] = tmp
    Signal_MC_Akzeptanz.Fill()

print(np.std(a3))
print(np.mean(a3))
plt.hist(a3, bins=50, alpha=0.8)
plt.title(r"Hitverteilung")
plt.xlabel(r'$Hits$')
plt.yscale('log')
plt.savefig('fig/1c.pdf')
plt.clf()

# Aufgabe d)

a4 = []
a4_x = []
a4_y = []
fill_me4 = np.zeros(1, dtype=float)
fill_me5 = np.zeros(1, dtype=float)
Signal_MC_Akzeptanz.Branch('x', fill_me4, 'Hits/D')
Signal_MC_Akzeptanz.Branch('y', fill_me5, 'Hits/D')
polargen2 = Polar_Normal(61321)
for i in a3:
    x = -1
    y = -1
    while x>10 or x<0 or y>10 or y<0:
        x = polargen2.random_normal(7, sigma_ort(i))[0]
        y = polargen2.random_normal(3, sigma_ort(i))[0]
    a4.append((x, y))
    a4_x.append(x)
    a4_y.append(y)
    fill_me4[0] = x
    fill_me5[0] = y
    Signal_MC_Akzeptanz.Fill()

#antplot
plt.plot(a4_x, a4_y, 'ko', markersize=1)
plt.title(r"Ortsverteilung")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig('fig/1d_ant.pdf')
plt.clf()

#ergibt diese Darstellung Sinn?
plt.hist2d(a4_x, a4_y, bins=100)
plt.colorbar()
plt.title("Ortsverteilung")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig('fig/1d_hist.pdf')
plt.clf()
# Aufgabe e)

Untergrund_MC = ROOT.TTree("Untergrund_MC", "Nicht so Geile Furz Ereignisse!")
fill_me6 = np.zeros(1, dtype=float)
fill_me7 = np.zeros(1, dtype=float)
fill_me8 = np.zeros(1, dtype=float)
Untergrund_MC.Branch('Anzahl Hits', fill_me6, 'Hits/D')
Untergrund_MC.Branch('x', fill_me7, 'Hits/D')
Untergrund_MC.Branch('y', fill_me8, 'Hits/D')
polargen3 = Polar_Normal(81732)
hits1 = []
x1 = []
y1 = []
print("Das kann noch ein wenig Dauern... Viel Spaß beim Warten!")
for i in range(50000):
    #Erzeuge die Hits, jewils in einer Iteration direkt zwei
    #Was sollgenau wem folgen? Ich erzeuge jetzt die Normalverteilung, nehme 10** diese Werte und nehme die Werte die 0 werden raus
    tmp = polargen3.random_normal(2, 1)
    while np.round(10**tmp[0])<=0 or np.round(10**tmp[1])<=0:
        tmp = polargen3.random_normal(2, 1)
    hits1.append(np.round(10**tmp[0]))
    hits1.append(np.round(10**tmp[1]))
    fill_me6[0] = np.round(10**tmp[0])
    Untergrund_MC.Fill()
    fill_me6[0] = np.round(10**tmp[1])
    Untergrund_MC.Fill()

print("Nein, es dauert noch länger....!")
for i in range(5000000):
    #1. Versuch
    tmp_x = 0
    tmp_y = 0
    rho = 0.5

    x_korr1 = -1
    y_korr1 = -1
    x_korr2 = -1
    y_korr2 = -1

    while x_korr1 < 0 or x_korr2 < 0 or y_korr1 <0 or y_korr2<0 or x_korr1>10 or x_korr2 >10 or y_korr1>10 or y_korr2>10:
        #Nochmal falls Dingens nicht auf dangens.
        tmp_x = polargen3.random_normal(0, 1)
        tmp_y = polargen3.random_normal(0, 1)
        rho = 0.5

        x_korr1 = np.sqrt(1-rho**2) * 3 * tmp_x[0] + rho * 3 * tmp_y[0] + 5 # geht das so?
        y_korr1 = 3 * tmp_y[0] + 5
        x_korr2 = np.sqrt(1-rho**2) * 3 * tmp_x[1] + rho * 3 * tmp_y[1] + 5
        y_korr2 = 3 * tmp_y[1] + 5

    x1.append(x_korr1)
    fill_me7[0] = x_korr1
    y1.append(y_korr1)
    fill_me8[0] = y_korr1
    Untergrund_MC.Fill()

    x1.append(x_korr2)
    fill_me7[0] = x_korr2
    y1.append(y_korr2)
    fill_me8[0] = y_korr2
    Untergrund_MC.Fill()


plt.hist(hits1, bins=50 ,alpha=0.8)
plt.title(r"Nebenereignisse")
plt.yscale('log')
#plt.xscale('log')
plt.xlabel(r'$N$')
plt.savefig('fig/1e_hits.pdf')
plt.clf()

plt.hist(x1, bins=50 ,alpha=0.8)
plt.title(r"X Abszissenachse")
plt.xlabel(r'$x$')
plt.savefig('fig/1e_x.pdf')
plt.clf()

plt.hist(y1, bins=50 ,alpha=0.8)
plt.title(r"Y Ordinatenachse")
plt.xlabel(r'$y$')
plt.savefig('fig/1e_y.pdf')
plt.clf()

#ergibt diese Darstellung Sinn?
plt.hist2d(x1, y1, bins=100)
plt.colorbar()
plt.title("Ortsverteilung Untergrund")
plt.xlabel("x")
plt.ylabel("y")

plt.savefig('fig/1e_hist.pdf')
plt.clf()

write_file.Write()
write_file.Close()
