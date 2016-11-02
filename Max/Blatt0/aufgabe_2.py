from numpy import *
import matplotlib.pyplot as plt
import matplotlib as mpl

#mpl.rcParams['lines.linewidth'] = 1



def nap(function, iterable):
    return array(list(map(function, iterable)))


def f(x):
    return (sqrt(9-x)-3)/x


x = logspace(-1,-20,num=20)  #list([10**e for e in range(-1,-21,-1)]) 

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.plot(x, nap(f,x), 'g-', label=r'\sqrt{(9-x)-3}} x^{-1}')

plt.title("Aufgabe 2")

plt.legend(loc="best")
plt.xscale("log")
plt.xlim(1e-21,1)
plt.ylim(0.05,-0.5)
plt.show()
