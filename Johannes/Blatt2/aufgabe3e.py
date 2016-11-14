import ROOT
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


## e)

#meine Verteilungsfunktion (Gleichverteilung)


def f(x_0, x_min, x_max, z):
    lenght = x_max-x_min
    my_array = []
    my_array.append(x_0)
    p = x_0
    for i in range(0,z-1):
        p = (137*p + 187) % (2**16)
        my_array.append(p)
    my_array = np.array(my_array)/(2**16)*lenght+x_min
    return my_array

data = np.load("empirisches_histogramm.npy")
plt.hist(data['bin_mid'], bins=np.linspace(0.,1.,50), weights=data['hist'])
print(data[0][0])




n = len(data)
m = 0
for i in range(0,n-1):
    m = m + data[i][1]

print(m)

a = f(56536, 0, m, 10000)

def f_hist(x):
    for i in range(0,len(x)-1):                                       #solange es Zufallszahlen gibt
        switch = False
        step = 0
        nextstep = 0
        while (switch == False):
            if (x[i] >= step) and (x[i] < step + data[nextstep][1]):  #sucht das Bin auf das die Zufallszahl fällt
                switch = True                                         #wenn gefunden: Suche wird unterbrochen
            else:
                step = step + data[nextstep][1]                       #wenn nicht gefunden: Gehe ein Intervall höher
                nextstep = nextstep + 1
        x[i] = (x[i] - step)/(data[nextstep][1])                      #die Zufallszahl fällt auf das Bin Nummer nextstep der Höhe data[nextstep][1] und die Zufallszahl wird auf dieses Intervall zugeschnitten
    return x                                                          #auf die Verteilung zugeschnittene Zufallszahlen werden wiedergegeben
#array wird nicht modifiziert....wieso auch immer...


a = f_hist(a)
canvas = ROOT.TCanvas("canvas", "Aufgabe 3e")
canvas.cd(1)
h = ROOT.TH1D("Zufall", "Zufall, bins=21", 50, 0, 1)
for tmp in a:
    h.Fill(tmp)
h.Draw()

canvas.Print("3e3.pdf")

plt.savefig('3e.pdf')
