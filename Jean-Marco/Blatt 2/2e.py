import ROOT
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class random_lcd:

    def __init__(self,a,b,m,x0):
        self.__a=a
        self.__b=b
        self.__m=m
        self.__x=x0

    def random_int(self):
        self.__x = (self.__a * self.__x + self.__b)%(self.__m)
        return self.__x
    def random_float(self):
        self.__x = (self.__a * self.__x + self.__b)%(self.__m)
        return self.__x/self.__m

a1=[]
zufall = ROOT.TRandom(34123) # Zufallsgenerator mit random seed
for i in range(5000):
    a1.append(zufall.Rndm())

canvas = ROOT.TCanvas("canvas", "Aufgabe 2e")

h1 = ROOT.TH1D("zufall1", "Zufallszahlen0", 30, min(a1), max(a1))
for tmp in a1:
    h1.Fill(tmp)
h1.Draw()

#2d

b1 = []
b2 = []
for i in range(5000):
    b1.append(zufall.Rndm())
    b2.append(zufall.Rndm())

plt.hist2d(b1, b2, bins=10)
plt.colorbar()
plt.title("5000 Zufallstupel als Histogram - 10 Bins")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig('2e_2.pdf')

plt.clf()

plt.hist2d(b1, b2, bins=30)
plt.colorbar()
plt.title("5000 Zufallstupel als Histogram - 30 Bins")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig('2e_3.pdf')

plt.clf()

c1=[]
c2=[]
c3=[]
for i in range(5000):
    c1.append(zufall.Rndm())
    c2.append(zufall.Rndm())
    c3.append(zufall.Rndm())


fig = plt.figure()
ax = fig.gca(projection='3d')

ax.view_init(14,39)
ax.scatter(c1, c2, c3, lw=0, s=5, c='r')
plt.title("500 Zufalltripel")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.savefig('2e_4.pdf')
