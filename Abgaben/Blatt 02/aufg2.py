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

canvas = ROOT.TCanvas("canvas", "Aufgabe 2a")

random1=random_lcd(1601,3456,10000,0)
random2=random_lcd(1601,3456,10000,100)
random3=random_lcd(1601,3456,10000,500)
random4=random_lcd(1601,3456,10000,1500)
random5=random_lcd(1601,3456,10000,5000)
random6=random_lcd(1601,3456,10000,10000)

a1 = []
for i in range(10000):
    a1.append(random1.random_float())

a2 = []
for i in range(10000):
    a2.append(random2.random_float())

a3 = []
for i in range(10000):
    a3.append(random3.random_float())

a4 = []
for i in range(10000):
    a4.append(random4.random_float())

a5 = []
for i in range(10000):
    a5.append(random5.random_float())

a6 = []
for i in range(10000):
    a6.append(random6.random_float())

canvas.Divide(3,2)

canvas.cd(1)
h1 = ROOT.TH1D("zufall1", "Zufallszahlen, Startwert = 0", 30, min(a1), max(a1))
for tmp in a1:
    h1.Fill(tmp)
h1.Draw()

canvas.cd(2)
h2 = ROOT.TH1D("zufall2", "Zufallszahlen, Startwert = 100", 30, min(a2), max(a2))
for tmp in a2:
    h2.Fill(tmp)
h2.Draw()

canvas.cd(3)
h3 = ROOT.TH1D("zufall3", "Zufallszahlen, Startwert = 500", 30, min(a3), max(a3))
for tmp in a3:
    h3.Fill(tmp)
h3.Draw()

canvas.cd(4)
h4 = ROOT.TH1D("zufall4", "Zufallszahlen, Startwert = 1500", 30, min(a4), max(a4))
for tmp in a4:
    h4.Fill(tmp)
h4.Draw()

canvas.cd(5)
h5 = ROOT.TH1D("zufall5", "Zufallszahlen, Startwert = 5000", 30, min(a5), max(a5))
for tmp in a5:
    h5.Fill(tmp)
h5.Draw()

canvas.cd(6)
h6 = ROOT.TH1D("zufall6", "Zufallszahlen, Startwert = 10000", 30, min(a6), max(a6))
for tmp in a6:
    h6.Fill(tmp)
h6.Draw()

canvas.Print("fig/2b_1.pdf")

###



random1=random_lcd(1601,3456,10000,0)

#2d

a1 = []
a2= []
for i in range(5000):
    a1.append(random1.random_float())
    a2.append(random1.random_float())

plt.hist2d(a1, a2, bins=50)
plt.colorbar()
plt.title("5000 Zufallstupel als Histogram - 50 Bins")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig('2c_1.pdf')

plt.clf()

#3d

b1=[]
b2=[]
b3=[]
for i in range(3000):
    b1.append(random1.random_float())
    b2.append(random1.random_float())
    b3.append(random1.random_float())


fig = plt.figure()
ax = fig.gca(projection='3d')

ax.view_init(14,39)
ax.scatter(b1, b2, b3, lw=0, s=5, c='r')
plt.title("3000 Zufalltripel")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.savefig('2c_2.pdf')

plt.clf()


###

a1=[]
zufall = ROOT.TRandom(34123) # Zufallsgenerator mit random seed
for i in range(5000):
    a1.append(zufall.Rndm())

canvas = ROOT.TCanvas("canvas", "Aufgabe 2e")

h1 = ROOT.TH1D("zufall1", "Zufallszahlen0", 30, min(a1), max(a1))
for tmp in a1:
    h1.Fill(tmp)
h1.Draw()
plt.savefig('fig/2e_1.pdf')

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
plt.savefig('fig/2e_2.pdf')

plt.clf()

plt.hist2d(b1, b2, bins=30)
plt.colorbar()
plt.title("5000 Zufallstupel als Histogram - 30 Bins")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig('fig/2e_3.pdf')

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
plt.savefig('fig/2e_4.pdf')

###

random1=random_lcd(1601,3456,10000, 0.9643972517176764
)
count=0
a1 = []
for i in range(10000):
    tmp = random1.random_float()
    a1.append(tmp)
    if tmp==0.5:
        count=count+1

#print(a1)

print("Vorkommen bei passenden Startwert:")
print(count)
print("Passende Startwerte:")
for i in range(10):
    a=1601
    b=3456
    m=10000
    print((m*i+5000-b)/a)
