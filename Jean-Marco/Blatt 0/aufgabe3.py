import numpy as np
import matplotlib.pyplot as plt

def f(x):
    a = x**3 + 1/3
    b = x**3 - 1/3
    return a-b

x = np.linspace(1, 0.2*10**6, 10000)
plt.title('Aufgabe 3a')
plt.xlabel(r'$x$')
plt.ylabel(r'$(x^3 + \frac{1}{3}) - (x^3 - \frac{1}{3})$')
#plt.xlim(-0.01, 1.01)
#plt.ylim(-0.1, 1.1)
plt.plot(x, f(x), 'b')
plt.plot(x, 0*x + 2/3, 'g-')
plt.plot(x, 0*x + 2*0.99/3, 'r-')
plt.plot(x, 0*x + 2*1.01/3, 'r-')
plt.savefig('3a')
np.savetxt('aufgabe3_a_1.txt', [x, f(x)])


plt.clf()

x = np.linspace(1, 10**5, 10000)
plt.title('Aufgabe 3a')
plt.xlabel(r'$x$')
plt.ylabel(r'$(x^3 + \frac{1}{3}) - (x^3 - \frac{1}{3})$')
#plt.xlim(-0.01, 1.01)
#plt.ylim(-0.1, 1.1)
plt.plot(x, f(x), 'b')
plt.plot(x, 0*x + 2/3, 'g-')
plt.plot(x, 0*x + 2*0.99/3, 'r-')
plt.plot(x, 0*x + 2*1.01/3, 'r-')
plt.savefig('3a_2')
np.savetxt('aufgabe3_a_2.txt', [x, f(x)])


plt.clf()
