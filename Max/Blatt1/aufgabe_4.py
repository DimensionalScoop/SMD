import numpy as np
import numpy.linalg as linalg
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import smd
from scipy.optimize import newton

smd.enable_tex_for_plotting()
plot_accuracy = 200
plot_frame = 7

μ = np.array((4, 2))
σ = np.array((3.5, 1.5))
cov = 4.2

ρ = cov / np.prod(σ)
print("a)", ρ)


# covariance matrix
Σ = np.array([
    [σ[0]**2, cov],
    [cov, σ[1]**2]])


def gauss(x):
    return smd.gauss_multivariate(x, Σ, μ)
prefactor = smd.gauss_multivariate_prefactor(Σ)


def generate_3D_plot_data():
    """Return (X,Y,Z) matrices. Rotates x,y by θ."""
    # Generate mesh for b)
    x = np.linspace(4 - plot_frame, 4 + plot_frame, plot_accuracy)
    y = np.linspace(2 - plot_frame, 2 + plot_frame, plot_accuracy)
    X, Y = np.meshgrid(x, y)

    # Fill matrix with values of the Gaussian at different positions
    Z = np.zeros((x.size, y.size))
    for i, f_x in enumerate(x):
        for j, f_y in enumerate(y):
            Z[j, i] = gauss((f_x, f_y))  # still strange; why do I have to switch j and i ?

    return (X, Y, Z)


plot_data = generate_3D_plot_data()

# Draw a contour plot of the whole gaussian
c = plt.contourf(*plot_data, cmap=cm.hot)
plt.colorbar(c)

# b) Draw a contour where Z is at e^-0.5, i.e. the ellipsis
plt.contour(*plot_data, [prefactor / np.sqrt(np.e)], colors="g")
plt.plot(0, 0, label="$e^{-0.5}$-Ellipse", color="g")  # cheat a legend for the contour plot

# c) Draw sigmas
plt.errorbar(*μ, xerr=σ[0], yerr=σ[1], fmt='g', label=r'$\mu \pm \sigma$')


# find angle for which minor diagonal vanishes
root = newton(lambda x: smd.rotate(Σ, x)[0, 1], 0)
Σ = smd.rotate(Σ, root)
assert np.abs(Σ[0, 1]) < 1e-7
assert np.abs(Σ[1, 0]) < 1e-7

σ = (np.sqrt(Σ[0, 0]), np.sqrt(Σ[1, 1]))

print("d) Angle:", root / np.pi, "*π")
print("σ_x':", σ[0])
print("σ_y':", σ[1])

plot_data = generate_3D_plot_data()
plt.contour(*plot_data, [prefactor / np.sqrt(np.e)], colors="m")
plt.plot(0, 0, label="$e^{-0.5}$-Ellipse", color="m")  # cheat a legend for the contour plot

# d) Draw sigmas
plt.errorbar(*μ, xerr=σ[0], yerr=σ[1], fmt='m', label=r'$\mu \pm \sigma^{,}$')

plt.gca().set_aspect('equal')
plt.legend(loc='best')
plt.savefig("fig/4c.pdf")
