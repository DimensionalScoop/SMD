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
data = pd.DataFrame()

data['x'] = array(sorted(append([-3, 0, 3], linspace(-10, 10, 997))))  # for c)

# Generate analytical data via uncertainties
a_analytical = correlated_values((1, 1), cov)
data['Analytical Nom'] = unp.nominal_values(f(data['x'], a_analytical))
data['Analytical Std'] = unp.std_devs(f(data['x'], a_analytical))

# Monte Carlo
samples = 10000
a_mc = random.multivariate_normal((1, 1), cov, samples)
# a plot visualizing the 2d normal distribution
plot = gg.qplot(a_mc[:, 0], a_mc[:, 1]) + gg.xlab('a0') + gg.ylab('a1')
plot.save("fig/4b-a.pdf")


def std_dev_mc(x_array):
    return_value = []
    for x in x_array:
        values = [f(x, a) for a in a_mc]
        nominal = mean(values)
        std_d = std(values, ddof=1)
        return_value.append(ufloat(nominal, std_d))
    return return_value


noms_with_stds_mc = smd.parallel_slice(std_dev_mc, data['x'])  # std_dev_mc(list(data['x']))
data['Monte Carlo Nom'] = unp.nominal_values(noms_with_stds_mc)
data['Monte Carlo Std'] = unp.std_devs(noms_with_stds_mc)
data['Relative Difference Nom'] = abs(data['Analytical Nom'] - data['Monte Carlo Nom']) / data['Analytical Nom']
data['Relative Difference Std'] = abs(data['Analytical Std'] - data['Monte Carlo Std']) / data['Analytical Std']

# Plot
data.drop('Monte Carlo Nom', 1).drop('Monte Carlo Std', 1).drop('Analytical Std', 1).drop('Analytical Nom', 1).plot.line(x='x')
plt.yscale('log')
plt.title("Monte Carlo vs. Analytical")
plt.savefig("fig/4b-diff.pdf")

# Print special values for c)
for k in range(-3, 3 + 1, 3):
    print(data[data['x'] == -k])
