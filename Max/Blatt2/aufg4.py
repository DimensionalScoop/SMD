from numpy import *
import uncertainties.unumpy as unp
from uncertainties import *
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import smd
import ggplot as gg
matplotlib.style.use('ggplot')


def f(x, a):
    return a[0] + a[1] * x

cov = [(0.2**2, -0.064 / 2), (-0.064 / 2, 0.2**2)]
data = pd.DataFrame(columns=["x", "Analytical", "Monte Carlo"])

data['x'] = append([-3, 0, 3], linspace(-10, 10, 997))  # for c)

# Generate analytical data via uncertainties
a_analytical = correlated_values((1, 1), cov)
data['Analytical'] = unp.std_devs(f(data['x'], a_analytical))

# Monte Carlo
samples = 10000
a_mc = random.multivariate_normal((1, 1), cov, samples)
# a plot visualizing the 2d normal distribution
plot = gg.qplot(a_mc[:, 0], a_mc[:, 1]) + gg.xlab('a0') + gg.ylab('a1')
plot.save("fig/4b-a.pdf")


def std_dev_mc(x_array):
    return_value = []
    for x in x_array:
        diff = 0
        for k in range(samples):
            diff += (f(x, (1, 1)) - f(x, a_mc[k]))**2 / samples  # without squaring all differences zero out
        return_value.append(sqrt(diff))
    return return_value


data['Monte Carlo'] = smd.parallel_slice(std_dev_mc, data['x'])  # std_dev_mc(list(data['x']))
data['Absolute Difference'] = abs(data['Analytical'] - data['Monte Carlo'])

# Plot
data.drop('Absolute Difference', 1).plot.line(x='x')
plt.title("Std Devs")
plt.savefig("fig/4b-b.pdf")

data.plot.line(x='x', y='Absolute Difference')
plt.yscale('log')
plt.title("Monte Carlo vs. Analytical")
plt.savefig("fig/4b-c.pdf")

for k in range(-3, 3 + 1, 3):
    print(data[data['x'] == -k])
