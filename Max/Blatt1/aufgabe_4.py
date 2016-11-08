import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import smd

smd.enable_tex_for_plotting()


μ = np.array((4, 2))
σ = np.array((3.5, 1.5))
cov = 4.2
# NO k_0 = 1 / (2 * np.pi * np.prod(σ))

ρ = cov / np.prod(σ)
print("a)", ρ)


# covariance matrix
Σ = np.array([
    [smd.variance_gauss(σ[0], μ[0]), cov],
    [cov, smd.variance_gauss(σ[1], μ[1])]])


# Generate mesh for b)
x = np.linspace(4 - 7, 4 + 7, 100 * 2)
y = np.linspace(2 - 7, 2 + 7, 100 * 2)
X, Y = np.meshgrid(x, y)


def gauss(x):
    return smd.gauss_multivariate(x, Σ, μ)
prefactor = smd.gauss_multivariate_prefactor(Σ)


# Fill matrix with values of the Gaussian at different positions
Z = np.zeros((x.size, y.size))
for i, f_x in enumerate(x):
    for j, f_y in enumerate(y):
        Z[j, i] = gauss((f_x, f_y))  # still strange; why do I have to switch j and i ?


# Draw a contour plot of the whole gaussian
c = plt.contourf(X, Y, Z, cmap=cm.hot)
plt.colorbar(c)

# Draw a contour where Z is at e^-0.5, i.a. the ellipsis
plt.contour(X, Y, Z, [prefactor / np.sqrt(np.e)])
plt.plot(0, 0, label="$e^{-0.5}$-Ellipse")  # cheat a legend for the contour plot

# Draw sigmas
plt.errorbar(*μ, xerr=σ[0], yerr=σ[1], fmt='g', label=r'$\mu \pm \sigma$')

plt.gca().set_aspect('equal')
plt.legend(loc='best')
plt.savefig("fig/4b.pdf")
