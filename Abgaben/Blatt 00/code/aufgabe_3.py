import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties.unumpy import (
    nominal_values as noms,
    std_devs as stds,
)


# 3. Aufgabe

plt.clf()


def h(x):
    return ((x**3 + 1 / 3) - (x**3 - 1 / 3))


def k(x):
    return (((3 + (x**3) / 3) - (3 - (x**3) / 3)) / x**3)


def p(x):
    return 2 / 3

x = np.linspace(10**4, 300000, 1000000)
plt.plot(x, h(x), 'b-', label='Numerisches Ergebnis')
plt.xscale('log')
#plt.axhline(y=2/3, color='r', linestyle='--')
plt.axhline(y=2 / 3 + 0.01 * 2 / 3, color='r', linestyle='--', label ='Abweichung von 1%')
plt.axhline(y=2 / 3 - 0.01 * 2 / 3, color='r', linestyle='--')
plt.xlim(10**4, 300000)
plt.ylim(-0.001, 1.02)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('3a.pdf')

plt.clf()

x = np.linspace(1.5 * 10**(-6), 10**(-4), 1000000)
plt.plot(x, k(x), 'b-', label='Numerisches Ergebnis')
plt.xscale('log')
#plt.axhline(y=2/3, color='r', linestyle='--')
plt.axhline(y=2 / 3 + 0.01 * 2 / 3, color='r', linestyle='--', label ='Abweichung von 1%')
plt.axhline(y=2 / 3 - 0.01 * 2 / 3, color='r', linestyle='--')
plt.xlim(1.5 * 10**(-6), 10**(-4))
plt.ylim(-0.002, 1.4)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('3b.pdf')

plt.clf()
