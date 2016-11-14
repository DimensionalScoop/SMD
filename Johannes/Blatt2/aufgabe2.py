import ROOT
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

## a)
def f(x_0, a, b, m, z):
    my_array = []
    my_array.append(x_0)
    p = x_0
    for i in range(0,z-1):
        p = (a*p + b) % m
        my_array.append(p)
    my_array = np.array(my_array)/m
    return my_array

x = f(1, 1601, 3456, 10000, 10000)
print(x)

def g(my_array1):
    my_list1 = list(my_array1)
    my_list2 = []
    for i in range(0,len(my_list1)-1):
        if (i%2 == 0):
            my_list2.append(my_list1[i])
    my_array1 = np.array(my_list2)
    return my_array1

def u(my_array1):
    my_list1 = list(my_array1)
    my_list2 = []
    for i in range(0,len(my_list1)):
        if (i%2 == 1):
            my_list2.append(my_list1[i])
    my_array1 = np.array(my_list2)
    return my_array1

def c1(my_array1):
    my_list1 = list(my_array1)
    if(len(my_list1) % 3 == 1):
        del my_list1[-1]
    if(len(my_list1) % 3 == 2):
        del my_list1[-1]
        del my_list1[-1]
    my_list2 = []
    for i in range(0,len(my_list1)):
        if (i%3 == 0):
            my_list2.append(my_list1[i])
    my_array1 = np.array(my_list2)
    return my_array1

def c2(my_array1):
    my_list1 = list(my_array1)
    if(len(my_list1) % 3 == 1):
        del my_list1[-1]
    if(len(my_list1) % 3 == 2):
        del my_list1[-1]
        del my_list1[-1]
    my_list2 = []
    for i in range(0,len(my_list1)):
        if (i%3 == 1):
            my_list2.append(my_list1[i])
    my_array1 = np.array(my_list2)
    return my_array1

def c3(my_array1):
    my_list1 = list(my_array1)
    if(len(my_list1) % 3 == 1):
        del my_list1[-1]
    if(len(my_list1) % 3 == 2):
        del my_list1[-1]
        del my_list1[-1]
    my_list2 = []
    for i in range(0,len(my_list1)):
        if (i%3 == 2):
            my_list2.append(my_list1[i])
    my_array1 = np.array(my_list2)
    return my_array1

x = f(1, 1601, 3456, 10000, 10000)
print(x)

## b)

canvas = ROOT.TCanvas("canvas", "Aufgabe 2b")
#canvas.Divide(3,2)

canvas.cd(1)
h = ROOT.TH1D("Zufall", "Zufall, bins=21", 21, min(x), max(x))
for tmp in x:
    h.Fill(tmp)
h.Draw()

canvas.Print("2b.pdf")
#guter Zufallszahlen-Generator?
#Nein, denn wie in dem Histogramm zu sehen ist (Binbreite durch Regel von Scott berechnet), werden manche Zahlenintervalle bevorzugt.
#Bei einer großen Anzahl an Zufallszahlen, angenommen 10000 sind viele genug, würde man von einer Gleichverteilung ausgehen.


# hängt von x_0 ab, aber nur insofern, dass es den Start der Reihenfolge definiert:
#Der Zufallsgenerator wird irgendwann mal wieder bei x_0 ankommen.
#Wenn dies passiert, wird sich die vorherige Reihenfolge der Zufallszahlen wiederholen.
#Demnach unterscheiden sich zwei Sätze von Zufallszahlen abhängig vom Startwert nur in den Zahlen, die zwischen den Startwerten generiert werden.
#Das Problem wird jedoch durch eine hohe Anzahl an Zufallszahlen minimiert.


# c)

x = g(f(1, 1601, 3456, 10000, 10000))
y = u(f(1, 1601, 3456, 10000, 10000))



plt.hist2d(x, y, bins=21)
plt.colorbar()
plt.savefig('2c1.pdf')

plt.clf()

x = c1(f(1, 1601, 3456, 10000, 10000))
y = c2(f(1, 1601, 3456, 10000, 10000))
z = c3(f(1, 1601, 3456, 10000, 10000))

fig = plt.figure()

ax = fig.add_subplot(111, projection ='3d')
ax.scatter(x, y, z, c='b', marker='o')

ax.view_init(elev= 0.5, azim = 20)

plt.savefig('2c2.pdf')

plt.clf()

## e)

zufall = ROOT.TRandom(8323246)  # Zufallsgenerator mit random seed
a = []

for i in range(10000):
    a.append(zufall.Integer(10000) + 1)

a = np.array(a)/10000

x = g(a)
y = u(a)



plt.hist2d(x, y, bins=21)
plt.colorbar()
plt.savefig('2c1root.pdf')

plt.clf()

x = c1(a)
y = c2(a)
z = c3(a)

fig = plt.figure()

ax = fig.add_subplot(111, projection ='3d')
ax.scatter(x, y, z, c='b', marker='o')

#ax.view_init(elev= 0.5, azim = 20)

plt.savefig('2c2root.pdf')

plt.clf()

canvas = ROOT.TCanvas("canvas", "Aufgabe 2e")
#canvas.Divide(3,2)

canvas.cd(1)
h = ROOT.TH1D("Zufall", "Zufall, bins=21", 21, min(a), max(a))
for tmp in a:
    h.Fill(tmp)
h.Draw()

canvas.Print("2e.pdf")

## f)

q = list(f(1/2, 1601, 3456, 10000, 10000))
print(q.count(1/2))

#viel Spaß 1/2 darzustellen xD
