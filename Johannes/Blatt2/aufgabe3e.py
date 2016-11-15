import ROOT
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from ggplot import *


# e)

# meine Verteilungsfunktion (Gleichverteilung)


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

print(m)

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

    # if 1 == 0:
    #     for i in range(len(x)):  # solange es Zufallszahlen gibt
    #         switch = False
    #         step = 0
    #         nextstep = 0
    #         while (switch == False):
    #             if (x[i] >= step) and (x[i] < step + data[nextstep][1]):  # sucht das Bin auf das die Zufallszahl fällt
    #                 switch = True  # wenn gefunden: Suche wird unterbrochen
    #             else:
    #                 step = step + data[nextstep][1]  # wenn nicht gefunden: Gehe ein Intervall höher
    #                 nextstep = nextstep + 1
    #         x[i] = (x[i] - step) / (data[nextstep][1])  # die Zufallszahl fällt auf das Bin Nummer nextstep der Höhe data[nextstep][1] und die Zufallszahl wird auf dieses Intervall zugeschnitten
    #     return x  # auf die Verteilung zugeschnittene Zufallszahlen werden wiedergegeben
# array wird nicht modifiziert....wieso auch immer...


a = list(f_hist(a))
canvas = ROOT.TCanvas("canvas", "Aufgabe 3e")
canvas.cd(1)
h = ROOT.TH1D("Zufall", "Zufall", 50, 0, 1)
for tmp in a:
    h.Fill(tmp)
h.Draw()

canvas.Print("3e3.pdf")

plt.savefig('3e.pdf')

plot1 = qplot(x=bin_mid_positions, y=bin_heights) + ggtitle("Der Peak, der keiner war")
plot2 = qplot(a) + ggtitle("Unsere Verteilung") + geom_histogram(binwidth=1 / 50)

plot1.save("3e.pdf")
plot2.save("3e3.pdf")
