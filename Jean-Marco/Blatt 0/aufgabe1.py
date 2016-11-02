import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.999, 1.001, 1000)
def a(x):
    return (1-x)**6

def b(x):
    return x**6-6*x**5+15*x**4-20*x**3+15*x**2-6*x+1

def horner(a, x):
    #Werte koeffizienten a0 bis an an Stelle x aus
    i=0
    f = []
    while i < len(a):
        if i==0:
            f.append(a[i])
        else:
            f.append(f[i-1]*x+a[i])
        i=i+1
    return f[-1]

plt.title('Aufgabe 1a - Direkt')
plt.xlabel(r'$x$')
plt.ylabel(r'$(1-x)^6$')
#plt.xlim(-0.01, 1.01)
#plt.ylim(-0.1, 1.1)
plt.plot(x, a(x))
plt.savefig('1a')

plt.clf()

plt.title('Aufgabe 1b - Ausmultipliziert')
plt.xlabel(r'$x$')
plt.ylabel(r'$x^6 - 6 x^5 + 15 x^4 - 20 x^3 + 15 x^2 - 6 x + 1$')
#plt.xlim(-0.01, 1.01)
#plt.ylim(-0.1, 1.1)
plt.plot(x, b(x))
plt.savefig('1b')


plt.clf()

plt.title('Aufgabe 1c - Horner')
plt.xlabel(r'$x$')
plt.ylabel('(1-x)^6')
#plt.xlim(-0.01, 1.01)
#plt.ylim(-0.1, 1.1)
a = [1, -6, 15, -20, 15, -6, 1]
plt.plot(x, horner(a, x))
plt.savefig('1c')
