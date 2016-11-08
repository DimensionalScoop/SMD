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
x = np.linspace(4 - 10, 4 + 10, 100)
y = np.linspace(2 - 10, 2 + 10, 100)
X, Y = np.meshgrid(x, y)


def gauss(x):
    return smd.gauss_multivariate(x, Σ, μ)
prefactor = smd.gauss_multivariate_prefactor(Σ)

# Exponent of the Gaussian
# F = k_0 * np.exp(-1 / 2 * (gauß_exp(X, μ[0], σ[0]) + gauß_exp(Y, μ[1], σ[1])))

# Fill matrix with values of the Gaussian at different positions
Z = np.zeros((x.size, y.size))
F = []
for i, f_x in enumerate(x):
    for j, f_y in enumerate(y):
        Z[i, j] = gauss((f_x, f_y))
        F.append((f_x, f_y, Z[f_x, f_y]))
F = np.array(F)

# Only draw contour where F(X,Y) = 1, i.a. the ellipsis
#plt.contour(X, Y, F, [prefactor / np.sqrt(np.e)])

plt.errorbar(*μ, xerr=σ[0], yerr=σ[1], fmt='g', label=r'$\mu \pm \sigma$')


plt.contourf(X, Y, Z, cmap=cm.jet)

plt.legend(loc='best')
plt.savefig("fig/4b.pdf")
