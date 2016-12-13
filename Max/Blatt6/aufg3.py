from numpy import *
import matplotlib.pyplot as plt

Temp = array([29.4, 26.7, 28.3, 21.1, 20, 18.3, 17.8, 22.2, 20.6, 23.9, 23.9, 22.2, 27.2, 21.7])
Wetter = array([2, 2, 1, 0, 0, 0, 1, 2, 2, 0, 2, 1, 1, 0])
Feuchte = array([85, 90, 78, 96, 80, 70, 65, 95, 70, 80, 70, 90, 75, 80])
Wind = array([0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1])
Fußball = array([0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0])

assert len(Temp) == len(Wetter)
assert len(Feuchte) == len(Wetter)
assert len(Feuchte) == len(Wind)
assert len(Fußball) == len(Wind)


def H(p, n):
    return -p / (p + n) * log2(p / (p + n)) - n / (p + n) * log2(n / (p + n))


def E(a, cut):
    Anti_Fußball = (0 == Fußball)
    p_1 = count_nonzero((a > cut) * Fußball)
    n_1 = count_nonzero((a > cut) * Anti_Fußball)
    p_2 = count_nonzero((a < cut) * Fußball)
    n_2 = count_nonzero((a < cut) * Anti_Fußball)
    return (p_1 + n_1) / len(Fußball) * H(p_1, n_1) + (p_2 + n_2) / len(Fußball) * H(p_2, n_2)


def gains(a, count_cuts):
    cuts = linspace(min(a), max(a), count_cuts)[1:-1]
    return (cuts, [H_S - E(a, cut) for cut in cuts])

E_W = 9 / 14 * H(3, 6) + 5 / 14 * H(3, 2)
H_S = H(9, 5)

gain_W = H_S - E(Wind, 0.5)

plt.plot(*gains(Temp, 200), label="Temperatur", color='r')
plt.plot(*gains(Wetter, 200), label="Wetter", color='y')
plt.plot(*gains(Feuchte, 200), label="Feuchte", color='b')
plt.plot(*gains(Wind, 200), label="Wind", color='g')
plt.legend(loc='best')
plt.ylabel("Informationsgewinn")
plt.xlabel("Normiertes Attribut (a.u.)")
plt.show()
