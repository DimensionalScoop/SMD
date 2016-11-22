import os
import numpy as np
from numpy import *
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from mpl_toolkits . mplot3d import Axes3D

import ROOT

def aufg1():

    if not os.path.exists("./build"):
        os.makedirs("./build")


    random_gen = ROOT.TRandom(1550)



#Aufgabenteil a

    def phi(gamma):
        """Calculates random Energy for Neutrino current.
        gamma: Exponent of the current / spectral index"""
        E = (1 - random_gen.Rndm())**(1/(gamma+1))
        return E

#    print(int(1e5))
    energy = np.zeros(1, dtype=float)
    energy_plot = []

    root_file = ROOT.TFile("./build/NeutrinoMC.root", "RECREATE")
    tree = ROOT.TTree("Signal_MC", "Signal_MC")
    tree.Branch("Energie", energy, "Energie/D")

    for i in range(int(1e5)):
        energy[0] = (phi(-2.7))
        tree.Fill()
        energy_plot.append(phi(-2.7))

    root_file.Write()
#    root_file.Close()
    print("Pink")

    plt.hist(energy_plot,bins=range(1,50),color='c',alpha=0.5,label='Energie-Verteilung')
    plt.xlabel(r'$Zufallszahl$',fontsize=16)
    plt.legend(loc='best')
    plt.savefig('./build/a.pdf')
    plt.clf()
    plt.clf()

#Aufgabenteil b

    def detector(E):
        P = (1-np.exp(-E/2))**3
        return P

    def Neumann_detect(quantity):
        u1 = []
        u2 = []
        for i in range(int(quantity)):
            u1.append(phi(-2.7))
            u2.append(random_gen.Rndm())

        distribution = []
        no_good = []
        for j in range(int(quantity)):
            if detector(u1[j]) > u2[j]:
                distribution.append(u1[j])
            else:
                no_good.append(u1[j])

        return distribution, no_good

    ENERGIE,nope = Neumann_detect(1e5)

    energy_akz = np.zeros(1, dtype=float)
    #root_file = ROOT.TFile("./build/NeutrinoMC.root", "RECREATE")
    tree2 = ROOT.TTree("Signal_MC_Akzeptanz", "Signal_MC_Akzeptanz")
    tree2.Branch("Energie", energy_akz, "Energie/D")

    for i in range(len(ENERGIE)):
        energy_akz[0] = ENERGIE[i]
        tree2.Fill()


    print("Fluffy")

#Aufgabenteil c

    def Polarmethode():
        v1 = (2*(random_gen.Rndm()) -1)
        v2 = (2*(random_gen.Rndm()) -1)
        x1 = 0
        x2 = 0
        if v1**2 + v2**2 < 1:
            s = (v1**2 + v2**2)
            theta = (np.arctan2(v2, v1))
            r = np.sqrt(s)
            v11 = (r*np.cos(theta))
            v22 = (r*np.sin(theta))
            x1 = (v11*np.sqrt(-2/s * np.log(s)))
            x2 = (v22*np.sqrt(-2/s * np.log(s)))

        return x1,x2

    def Normal_Hits(mean,sigma):
        """Generates normal distributed random numbers with mean and standard deviation sigma"""
        if len(mean) == len(sigma):
            quantity = len(mean)
            verteilung_x1 = []
    #        verteilung_x2 = []

            for i in range(quantity):
                tryagain(i,verteilung_x1,mean,sigma)

        return verteilung_x1 #,verteilung_x2


    def tryagain(i,verteilung_x1,mean,sigma):
            x1,x2 = Polarmethode()
            if int(sigma[i]*x1 + mean[i]) > 0: # and int(sigma[i]*x2 + mean[i]) > 0:
                verteilung_x1.append(int(sigma[i]*x1 + mean[i]))
            #    verteilung_x1.append(int(sigma[i]*x2 + mean[i]))

        #        verteilung_x2.append(int(sigma[i]*x2 + mean[i]))
                return verteilung_x1 #,verteilung_x2
            else:
                return tryagain(i,verteilung_x1,mean,sigma)



    mean = []
    sigma = []
    for E in ENERGIE:
        mean.append(10*E)
        sigma.append(2*E)

    print("Unicorns")
    hits_x = Normal_Hits(mean,sigma)
    print(len(mean),len(hits_x))

    HITS = np.zeros(1, dtype=float)
    #root_file = ROOT.TFile("./build/NeutrinoMC.root", "RECREATE")
    #tree2 = ROOT.TTree("Signal_MC_Akzeptanz", "Signal_MC_Akzeptanz")
    tree2.Branch("AnzahlHits", HITS, "AnzahlHits/D")

    for i in range(len(hits_x)):
        HITS[0] = hits_x[i]
        tree2.Fill()


    print("Dancing")

    root_file.Write()
    root_file.Close()


#Aufgabe d

    def Quad_detect(mean_x,mean_y,sigma):
        """Generates normal distributed random numbers with mean and standard deviation sigma in a 10x10 Detector"""

        quantity = len(sigma)
        verteilung_x1 = []
        verteilung_x2 = []

        for i in range(quantity):
            verteilung_x1.append(tryagain2(i,mean_x,sigma))
            verteilung_x2.append(tryagain3(i,mean_y,sigma))
            verteilung_x1.append(tryagain3(i,mean_x,sigma))
            verteilung_x2.append(tryagain2(i,mean_y,sigma))

        return verteilung_x1,verteilung_x2


    def tryagain2(i,mean_x,sigma):
            x1,x2 = Polarmethode()
            if sigma[i]*x1 + mean_x < 10 or sigma[i]*x1 + mean_x > 0:
                helps = ((sigma[i]*x1 + mean_x))
                return helps
            else:
                return tryagain2(i,mean_x,sigma)

    def tryagain3(i,mean_x,sigma):
            x1,x2 = Polarmethode()
            if sigma[i]*x2 + mean_x < 10 or sigma[i]*x2 + mean_x > 0:
                helps = ((sigma[i]*x2 + mean_x))
                return helps
            else:
                return tryagain3(i,mean_x,sigma)



    mean_x = 7
    mean_y = 3
    sigma_d = []
    for N in hits_x:
        sigma_d.append(1/(np.log10(N+1)))

    #print(sigma_d)
    print("On")
    location_x,location_y = Quad_detect(mean_x,mean_y,sigma_d)
    #print(location_x)
    print("Rainbows")
    #print(len(test))
    #print(len(test)+len(nope))
    #print(detect_test)
    plt.hist(np.log(energy_plot),bins=np.linspace(1,10,50),color='c',alpha=0.5,label='Energie-Verteilung vorher')
    plt.hist(np.log(ENERGIE),bins=np.linspace(1,10,50),color='r',alpha=0.5,label='Energie-Verteilung nachher')
    plt.hist(np.log(hits_x),bins=np.linspace(1,10,50),color='y',alpha=0.5,label='Hits')


    #plt.xscale('log')
    plt.yscale('log')
    plt.xlabel(r'$Zufallszahl$',fontsize=16)
    plt.legend(loc='best')
    plt.savefig('./build/b.pdf')
    plt.clf()
    plt.clf()


    plt.hist2d(location_x, location_y, bins=50,norm=LogNorm())
    plt.colorbar()
    plt.savefig('./build/d.pdf')
    plt.clf()
    plt.clf()

#    def PseudoNeumann(limit,altitude,quantity):
#        """Generates random numbers obeying a given histogramm.
#        limit: Bin-Mitten des Datensatzes
#        altitude: Bin-Höhen des Datensatzes
#        quantity: quantity of random numbers"""
#
#        u1 = [] #Zufallszahlen "x"-Richtung
#        u2 = [] #Zufallszahlen "y"-Richtung
#
#        for i in range(quantity):
#            u1.append(randomT_generator.Rndm())
#            u2.append(randomT_generator.Rndm())
#
#        altitude = altitude / max(altitude) #Bin-Höhen auf 1 normieren
#
#        distribution = []
#
#        BINS = np.linspace(0. , 1., 49)
#        intervall = abs(BINS[2]-BINS[1])/2
#
#        for j in range(len(limit)):
#            for i in range(len(u1)):
#                if abs(u1[i] - limit[j]) < intervall and altitude[j] > u2[i]: #Erster Teil überprüft zu welchem Bin die #Zufallszahl gehört und der zweite Teil überprüft, ob die zweite Zufallszahl kleiner als die dortige Bin-Höhe ist #und nur dann wird die Zufallszahl zugelassen.
#                    distribution.append(u1[i])
#
#        return distribution

#Alternative Implementierung für selbes Prinzip...
#    def PseudoNeumann2(limit,altitude,quantity):
#        """Generates random numbers obeying a given histogramm.
#        limit: borders of the bins
#        altitude: value of the bins
#        quantity: quantity of random numbers"""
#        luckynumbers = []
#        random_gen = ROOT.TRandom(22281) # Zufallsgenerator mit random seed
#        for i in range(quantity):
#            luckynumbers.append( (random_gen.Rndm() , random_gen.Rndm()) )
#
#        altitude = altitude / max(altitude) #Bin-Höhen auf 1 normieren
#
#        distribution = []
#
#        for i in luckynumbers:
#            j = (np.argmax(limit > i[0]) -1) #Erster Teil überprüft zu welchem Bin die Zufallszahl gehört
#            if i[1] < altitude[j] : #der zweite Teil überprüft, ob die zweite Zufallszahl kleiner als die dortige Bin-Höhe ist und nur dann wird die Zufallszahl zugelassen.
#                distribution.append(i[0])
#
#
#        return distribution

#    plt.hist(data['bin_mid'], BiN, weights=y_hehe , color='c',alpha=0.5,label='Datensatz')
#    plt.hist(test2,BiN,color='r',alpha=0.5,label='Zufallszahlen')
#    plt.xlabel(r'$x$',fontsize=16)
#    plt.legend(loc='upper left')
#    plt.savefig('./build/e2.pdf')
#    plt.clf()
#    plt.clf()
#
#    plt.hist(data['bin_mid'], BiN, weights=y_hehe , color='c',alpha=0.5,label='Datensatz')
#    plt.hist(test1,BiN,color='r',alpha=0.5,label='Zufallszahlen')
#    plt.xlabel(r'$x$',fontsize=16)
#    plt.legend(loc='upper left')
#    plt.savefig('./build/e.pdf')
#    plt.clf()
#    plt.clf()


if __name__ == '__main__':
    aufg1()

#the end
