import numpy as np
import matplotlib.pyplot as plt

def f(a0, d, psi):
    return a0 * np.cos(psi+d)

def f2(a1, a2, psi):
    return a1 * np.cos(psi) + a2*np.sin(psi)

x = np.linspace(0, 2*np.pi)
plt.plot(x, f(-0.086008, 1.1195615, x))
plt.plot(x, f2(-0.03751, 0.07740, x))
u = np.array([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330])
u = u/360 * 2*np.pi
v = np.array([-0.032, 0.010, 0.057, 0.068, 0.076, 0.080, 0.031, 0.005, -0.041, -0.09, -0.088, -0.074])
plt.plot(u,v,'k.')
plt.savefig('2d.pdf')
