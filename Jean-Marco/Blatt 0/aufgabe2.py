import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (np.sqrt(9-x)-3)/x


y = np.logspace(-1, -20, 20)
x = (-1)*np.linspace(-1, -20, 20)
plt.title('Aufgabe 2')
plt.xlabel(r'$x = 10^{-n}$')
plt.ylabel(r'$\frac{\sqrt{9-x}-3}{x}$')
#plt.xlim(-0.01, 1.01)
#plt.ylim(-0.1, 1.1)
plt.plot(x, f(y), 'go')
plt.plot(x, -1/6+0*x, 'r-')
plt.savefig('2a')
np.savetxt('aufgabe2.txt', [y, f(y)])
np.savetxt('aufgabe2_abw.txt', [y, abs(f(y)-1/6)/(1/6)])


plt.clf()

y = np.logspace(-0, -13, 13)
x = (-1)*np.linspace(-0, -13, 13)
plt.plot(x, abs(f(y)+(1/6))/(1/6), 'go')
plt.savefig('2a_abw')
