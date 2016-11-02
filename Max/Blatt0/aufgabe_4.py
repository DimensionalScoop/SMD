import numpy as np
import numpy
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.constants import alpha,eV,electron_mass

#mpl.rcParams['lines.linewidth'] = 1


def nap(function, iterable):
    return [function(x) for x in iterable]#np.array(list(map(function, iterable)))


def diff_cross_secion(beta,theta,s):
    return alpha**2/s*(2+np.sin(theta)**2)/(1-beta**2*np.cos(theta)**2)

def diff_cross_secion_improved(beta,theta,s):
    return alpha**2/s*(2+np.sin(theta)**2)/(np.cos(theta)**2/gamma**2+np.sin(theta)**2)



E_e = 50e9*eV
s = (2*E_e)**2
gamma = E_e/electron_mass
beta = np.sqrt(1-pow(gamma,-2))

x = np.linspace(np.pi-1e-7,np.pi+1e-7,num=1000)


plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.plot(x, nap(lambda theta:diff_cross_secion_improved(beta,theta,s),x), 'm-', label=r'Besser')
plt.plot(x, nap(lambda theta:diff_cross_secion(beta,theta,s),x), 'b-', label=r'Naiv')

plt.title("Aufgabe 4")

plt.legend(loc="best")
plt.yscale("log")
plt.xlabel(r"\theta")
plt.ylabel(r"$\frac{\mathrm{d}\sigma}{\mathrm{d}\Omega}$")
# plt.xlim(1e-21,1)
# plt.ylim(-0.1,1.4)
# plt.show()
plt.savefig("figs/aufgabe_4a.pdf")
