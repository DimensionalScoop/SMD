import numpy as np
import matplotlib.pyplot as plt

def f(x):
    c = 299792458
    a = 7.2973525664 * 10**(-3)
    s = (2*50*10**9 *1.6021766209*10**(-19))**2
    g = (50*10**9)/(511*10**3) * c**2

    e1 = a**2 / s
    e2 = 2 + np.sin(x)**2
    e3 = 1 - (1-g**(-2)) * np.cos(x)**2

    return e1 * (e2)/(e3)


def fneu(x):
    c = 299792458
    a = 7.2973525664 * 10**(-3)
    s = (2*50*10**9 *1.6021766209*10**(-19))**2
    g = (50*10**9)/(511*10**3) * c**2

    e1 = a**2 / s
    e2 = 2 + np.sin(x)**2
    e3 = 1/g**2 + (1-g**(-2)) * np.sin(x)**2

    return e1 * (e2)/(e3)

#x = np.linspace(0.0000001, -0.0000001, 1000000)
x = np.linspace(0.0000001, 0.00000001, 1000000)

plt.title('Aufgabe 4c - Original')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\sigma$')
#plt.xlim(0, 2*10**27)
#plt.ylim(-0.1, 1.1)
plt.plot(x, f(x), 'b')
#plt.axvline(0, color='k', linestyle='--')
#plt.axvline(np.pi, color='k', linestyle='--')
#plt.plot(x, 0*x + 2/3, 'g-')
#plt.plot(x, 0*x + 2*0.99/3, 'r-')
#plt.plot(x, 0*x + 2*1.01/3, 'r-')
plt.savefig('4')
#np.savetxt('aufgabe3_a_1.txt', [x, f(x)])
print(f(2))

plt.clf()

#x = np.linspace(0.0000001, -0.0000001, 1000000)
x = np.linspace(0.0000001, 0.00000001, 1000000)

plt.title('Aufgabe 4c) - Umgeformt')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$\sigma$')
#plt.xlim(-0, 3.3)
#plt.ylim(-0.1, 1.1)
plt.plot(x, fneu(x), 'b')
#plt.axvline(0, color='k', linestyle='--')
#plt.axvline(np.pi, color='k', linestyle='--')
#plt.plot(x, 0*x + 2/3, 'g-')
#plt.plot(x, 0*x + 2*0.99/3, 'r-')
#plt.plot(x, 0*x + 2*1.01/3, 'r-')
plt.savefig('4_2')
#np.savetxt('aufgabe3_a_1.txt', [x, f(x)])
print(f(2))
