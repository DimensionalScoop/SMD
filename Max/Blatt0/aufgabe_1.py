from numpy import *
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['lines.linewidth'] = 0.3

x = linspace(0.999, 1.001, num=1000)


def nap(function, iterable):
    return array(list(map(function, iterable)))


def a(x):
    return pow((1 - x),6)


def b(x):
    return x**6 - 6 * x**5 + 15 * x**4 - 20 * x**3 + 15 * x**2 - 6*x + 1


def c(x):
    return x * (x * (x * (x * (x * (x - 6) + 15) - 20) + 15) - 6) + 1

plt.title("Aufgabe 1")
plt.plot(x, nap(b,x), 'g-', label="Naiv")
plt.plot(x, nap(c,x), 'b-', label="Horner")
plt.plot(x, nap(a,x), 'r-', label="(1-x)^6")

plt.yscale("log")
plt.legend(loc="best")
plt.show()
