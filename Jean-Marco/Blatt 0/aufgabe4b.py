import numpy as np
import matplotlib.pyplot as plt

def f(x):
    c = 299792458

    g = (50*10**9)/(511*10**3) * c**2
    b = np.sqrt(1-g**(-2))
    return ((1-3*b**2)*np.sin(2*x)) / ( (b**2 * np.cos(x)**2-1)*(2+np.sin(x)**2) )



x = np.linspace(0.01, np.pi-0.01, 1000000)
plt.title('Aufgabe 4e')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\kappa$')
#plt.xlim(-0, 3.3)
#plt.ylim(-0.1, 1.1)
plt.plot(x, f(x), 'b')
plt.axvline(0.1, color='k', linestyle='--')
plt.axvline(np.pi-0.1, color='k', linestyle='--')
#plt.plot(x, 0*x + 2/3, 'g-')
#plt.plot(x, 0*x + 2*0.99/3, 'r-')
#plt.plot(x, 0*x + 2*1.01/3, 'r-')
plt.savefig('4e')
#np.savetxt('aufgabe3_a_1.txt', [x, f(x)])


plt.clf()
