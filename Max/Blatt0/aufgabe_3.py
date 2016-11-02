import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

#mpl.rcParams['lines.linewidth'] = 1


def nap(function, iterable):
    return [function(x) for x in iterable]#np.array(list(map(function, iterable)))


def a(x):
    return (x**3+1/3)-(x**3-1/3)

def b(x):
    return ((3+x**3/3) - (3-x**3/3))/x**3

x = np.logspace(-4,-6,num=10000)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.plot(x, [0]*len(x), 'b-', label=r'Nulllinie')
plt.plot(x, nap(a,x), 'g-', label=r'(x^3+1/3)-(x^3-1/3)')
plt.plot(x, nap(b,x), 'y-', label=r'((3+x^3/3) - (3-x^3/3))/x^3')

plt.title("Aufgabe 3")

plt.legend(loc="best")
plt.xscale("log")
# plt.xlim(1e-21,1)
plt.ylim(-0.1,1.4)
plt.show()
