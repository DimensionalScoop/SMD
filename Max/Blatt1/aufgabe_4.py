import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


#########
# Ellipse ist noch nicht korrekt! Wir haben die Formel für die unkorrelierte Gaussian benutzt!
#########


plt.rc('text', usetex=True)
plt.rc('font', family='serif')

μ = np.array((4, 2))
σ = np.array((3.5, 1.5))
cov = 4.2

k_0 = 1 / (2 * np.pi * np.prod(σ))

ρ = cov / np.prod(σ)
print("a)", ρ)


def gauß_exp(x, σ, μ):
    """Return exponent of a Gaussian"""
    return (x - μ)**2 / σ**2

# Generate mesh for b)
x = np.linspace(4 - 5, 4 + 5, 1000)
y = np.linspace(2 - 5, 2 + 5, 1000)
X, Y = np.meshgrid(x, y)

# Exponent of the Gaussian
F = k_0 * np.exp(-1 / 2 * (gauß_exp(X, μ[0], σ[0]) + gauß_exp(Y, μ[1], σ[1])))

# Only draw contour where F(X,Y) = 1, i.a. the ellipsis
plt.contour(X, Y, F, [k_0 / np.sqrt(np.e)])

plt.errorbar(*μ, xerr=σ[0], yerr=σ[1], fmt='g', label=r'$\mu \pm \sigma$')

plt.legend(loc='best')

plt.savefig("fig/4b.pdf")
