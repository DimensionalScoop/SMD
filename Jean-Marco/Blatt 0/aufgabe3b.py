import numpy as np
import matplotlib.pyplot as plt

def f(x):
    a = 3+x**3/3
    b = 3-x**3/3
    return (a-b)/x**3

x = np.linspace(-0.0002, 0.0002, 100000)
plt.title('Aufgabe 3b - Direkt')
plt.xlabel(r'$x$')
plt.ylabel(r'$\frac{(3+\sqrt{x^3}{3}) - (3 - \frac{x^3}{3})}{x^3}$')
#plt.xlim(-0.01, 1.01)
#plt.ylim(-0.1, 1.1)
plt.plot(x, f(x), 'b')
plt.plot(x, 0*x + 2/3, 'g-')
plt.plot(x, 0*x + 2*0.99/3, 'r-')
plt.plot(x, 0*x + 2*1.01/3, 'r-')
plt.savefig('3b')
np.savetxt('aufgabe3_b_1.txt', [x, f(x)])


plt.clf()

x = np.linspace(-0.00004, 0.00004, 1000000)
plt.title('Aufgabe 3b')
plt.xlabel(r'$x$')
plt.ylabel(r'$(x^3 + \frac{1}{3}) - (x^3 - \frac{1}{3})$')
#plt.xlim(-0.01, 1.01)
#plt.ylim(-0.1, 1.1)
plt.plot(x, f(x), 'b')
plt.plot(x, 0*x + 2/3, 'g-')
plt.plot(x, 0*x + 2*0.99/3, 'r-')
plt.plot(x, 0*x + 2*1.01/3, 'r-')
plt.savefig('3b_2')
np.savetxt('aufgabe3_b_2.txt', [x, f(x)])


plt.clf()
