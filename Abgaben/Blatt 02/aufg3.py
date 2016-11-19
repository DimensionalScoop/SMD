import ROOT
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from ggplot import *
import pandas as pd

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

a1 = []
for i in range(10000):
    a1.append(transform_a(zufall.Rndm()))

aunw = np.linspace(2,7,10)

plt.hist(a1)
plt.title(r"Gleichverteilung 3a - Exemplarisch von $x_{min} = 2$ bis $x_{max} = 7$")
plt.plot(aunw, aunw*0+1000, '-r')
plt.savefig('fig/3a.pdf')

plt.clf()

a2 = []
for i in range(100000):
    a2.append(transform_b(zufall.Rndm()))

plt.hist(a2, bins=100)
plt.title(r"Gleichverteilung 3b - Exemplarisch für $\tau = 100$")
plt.savefig('fig/3b.pdf')

plt.clf()

a3 = []
for i in range(100000):
    a3.append(transform_c(zufall.Rndm()))
plt.hist(a3, bins=80)
plt.title(r"Gleichverteilung 3c - $x_{min} = 2$ bis $x_{max} = 7$ und $n = 4$")
plt.savefig('fig/3c.pdf')

plt.clf()

a4 = []
for i in range(10000):
    a4.append(transform_d(zufall.Rndm()))
plt.hist(a4, bins=range(-30,30) ,alpha=0.8)
plt.title(r"Gleichverteilung 3d")
plt.savefig('fig/3d.pdf')

plt.clf()

##### --- ####



def f(x_0, x_min, x_max, z):
    lenght = x_max - x_min
    my_array = []
    my_array.append(x_0)
    p = x_0
    for i in range(0, z - 1):
        p = (137 * p + 187) % (2**16)
        my_array.append(p)
    my_array = np.array(my_array) / (2**16) * lenght + x_min
    return my_array

data = np.load("empirisches_histogramm.npy")
plt.hist(data['bin_mid'], bins=np.linspace(0., 1., 50), weights=data['hist'])
print(data[0][0])


n = len(data)
m = 0
bin_width = 1 / 50  # XXX: BIN WIDTH?
bin_end_hights = []
bin_heights = []
bin_mid_positions = []
for i in range(len(data)):
    m = m + data[i][1]
    bin_mid_positions.append(data[i][0])
    bin_heights.append(data[i][1])
    bin_end_hights.append(m)


a = np.random.randint(0, m, size=100000)  # f(56536, 0, m, 10000)


def f_hist(x):
    for rnd in x:
        assert rnd >= 0
        assert rnd <= m

        for i in range(1, len(bin_end_hights)):
            previous_bin = bin_end_hights[i - 1]
            current_bin = bin_end_hights[i]

            if i == 1 and rnd < previous_bin:
                relativ_position_in_bin = (rnd - 0) / previous_bin
                absolute_position_in_bin = relativ_position_in_bin * bin_width - bin_width / 2
                yield bin_mid_positions[i] + absolute_position_in_bin
                break
            elif rnd >= previous_bin and rnd < current_bin:
                relativ_position_in_bin = (rnd - previous_bin) / (current_bin - previous_bin)
                absolute_position_in_bin = relativ_position_in_bin * bin_width - bin_width / 2
                yield bin_mid_positions[i] + absolute_position_in_bin
                break
            else:
                assert i is not len(bin_end_hights) - 1


a = list(f_hist(a))
canvas = ROOT.TCanvas("canvas", "Aufgabe 3e")
canvas.cd(1)
h = ROOT.TH1D("Zufall", "Zufall", 50, 0, 1)
for tmp in a:
    h.Fill(tmp)
h.Draw()

canvas.Print("fig/3e3.pdf")

#plt.savefig('3e.pdf')


histo = []

for pos, height in zip(bin_mid_positions, bin_heights):
    histo.extend([pos] * int(height))

plot1 = qplot(histo) + ggtitle("Der Peak, der keiner war") + geom_histogram(binwidth=1 / 50)
plot1.save("fig/3e-orginale-daten.pdf")

plot2 = qplot(a) + ggtitle("Unsere Verteilung") + geom_histogram(binwidth=1 / 50)
plot2.save("fig/3e3.pdf")
