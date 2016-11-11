import numpy as np
import numpy.linalg as linalg
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import smd
from scipy.optimize import newton
from matplotlib.lines import Line2D
import scipy.integrate as integrate

smd.enable_tex_for_plotting()
plot_accuracy = 70
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


# f)
g = lambda x: integrate.quad(lambda y: gauss((x, y)), -np.inf, np.inf)[0]  # unnecessarily expensive, but reliable
h = lambda y: integrate.quad(lambda x: gauss((x, y)), -np.inf, np.inf)[0]


def f_x_y(x):
    result = gauss(x) / h(x[1])
    assert np.size(result) == 1
    return result


def f_y_x(x):
    return gauss(x) / g(x[0])


def generate_3D_plot_data(func):
    """Return (X,Y,Z) matrices. Rotates x,y by θ."""
    # Generate mesh for b)
    x = np.linspace(4 - plot_frame, 4 + plot_frame, plot_accuracy)
    y = np.linspace(2 - plot_frame, 2 + plot_frame, plot_accuracy)
    X, Y = np.meshgrid(x, y)

    # Fill matrix with values of the Gaussian at different positions
    Z = np.zeros((x.size, y.size))
    for i, f_x in enumerate(x):
        for j, f_y in enumerate(y):
            Z[j, i] = func((f_x, f_y))  # still strange; why do I have to switch j and i ?

    return (X, Y, Z)


plot_data_f_x_y = generate_3D_plot_data(f_x_y)
plot_data_f_y_x = generate_3D_plot_data(f_y_x)
plot_data_cov = generate_3D_plot_data(gauss)

# Draw a contour plot of the whole gaussian
c = plt.contourf(*plot_data_cov, cmap=cm.hot)
plt.colorbar(c)

# b) Draw a contour where Z is at e^-0.5, i.e. the ellipsis
plt.contour(*plot_data_cov, [prefactor / np.sqrt(np.e)], colors="g")
plt.plot(0, 0, label="$e^{-0.5}$-Ellipse", color="g")  # cheat a legend for the contour plot

# c) Draw sigmas
plt.errorbar(*μ, xerr=σ[0], yerr=σ[1], fmt='g', label=r'$\mu \pm \sigma$')


# find angle for which minor diagonal vanishes
root = newton(lambda x: smd.rotate(Σ, x)[0, 1], 0)
Σ = smd.rotate(Σ, root)
assert np.abs(Σ[0, 1]) < 1e-7
assert np.abs(Σ[1, 0]) < 1e-7

σ_new = (np.sqrt(Σ[0, 0]), np.sqrt(Σ[1, 1]))

print("d) Angle:", root / np.pi, "*π")
print("σ_x':", σ_new[0])
print("σ_y':", σ_new[1])


# d) Draw sigmas
plt.errorbar(*μ, xerr=σ_new[0], yerr=σ_new[1], fmt='m', label=r'$\mu \pm \sigma^{,}$')


plt.gca().set_aspect('equal')
plt.legend(loc='best')
plt.savefig("fig/4c.pdf")
plt.clf()

# e) Draw angle

fig = plt.figure()  # seems like some things can't be done without OO
ax = fig.add_subplot(1, 1, 1)

# plot ellipses again
plot_data_new = generate_3D_plot_data(gauss)
plt.contour(*plot_data_new, [prefactor / np.sqrt(np.e)], colors="m")
plt.plot(0, 0, label="$e^{-0.5}$-Ellipse", color="m")  # cheat a legend for the contour plot

plt.contour(*plot_data_cov, [prefactor / np.sqrt(np.e)], colors="g")
plt.plot(0, 0, label="$e^{-0.5}$-Ellipse", color="g")  # cheat a legend for the contour plot


offset = 0

x_new = (μ[0], μ[0] + 5)
y_new = (μ[1] + offset, μ[1] + offset)

x_cov = (μ[0], μ[0] + 5 * np.cos(root))
y_cov = (μ[1] + offset, μ[1] + 5 * np.sin(root) + offset)


# Draw lines
line_1 = Line2D(x_cov, y_cov, linewidth=1, linestyle="-", color="black")
line_2 = Line2D(x_new, y_new, linewidth=1, linestyle="-", color="black")

ax.add_line(line_1)
# ax.add_line(line_2)
ax.text(x_new[0] + 1.5, y_new[0] + 0.1, r'$\theta$', color="black")

plt.errorbar(*μ, xerr=σ_new[0], yerr=σ_new[1], fmt='red', label=r'Hauptachsen')

plt.gca().set_aspect('equal')
plt.legend(loc='best')
plt.savefig("fig/4e.pdf")


plt.clf()


# Draw a contour plot of conditional prop xy
c = plt.contourf(*plot_data_f_x_y, cmap=cm.hot)
plt.colorbar(c)

# b) Draw a contour where Z is at e^-0.5, i.e. the ellipsis
plt.contour(*plot_data_f_x_y, [prefactor / np.sqrt(np.e)], colors="g")

plt.gca().set_aspect('equal')
plt.legend(loc='best')
plt.savefig("fig/4f-1.pdf")

plt.clf()


# Draw a contour plot of conditional prop yx
c = plt.contourf(*plot_data_f_y_x, cmap=cm.hot)
plt.colorbar(c)

plt.gca().set_aspect('equal')
plt.legend(loc='best')
plt.savefig("fig/4f-2.pdf")
