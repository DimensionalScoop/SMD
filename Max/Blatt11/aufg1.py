import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def kolmo(size, lam):
    sigma = np.sqrt(lam)
    s1 = np.random.poisson(lam, size)
    s2 = np.rint(np.random.normal(lam, sigma, size))  # Zufallszahlen
    s1_hist = np.histogram(s1, bins=100, range=(lam - 5 * sigma, lam + 5 * sigma), density=True)  # Histogrammieren
    s2_hist = np.histogram(s2, bins=100, range=(lam - 5 * sigma, lam + 5 * sigma), density=True)
    s1_cum = np.cumsum(s1_hist[0])  # Kumullierte Summe
    s2_cum = np.cumsum(s2_hist[0])
    diff = np.abs(s1_cum - s2_cum)
    d_max = np.max(diff)
    test_val = np.sqrt(size**2 / (2 * size)) * d_max
    return test_val


def K_alpha(alpha):
    return np.sqrt(np.log(2 / alpha) / 2)

for a in [0.05, 0.025, 0.001]:
    target = K_alpha(a)
    first_occurance = 0
    for i in range(1, 10000):
        if kolmo(10000, i) < target:
            first_occurance = i
            break

    size = 10
    neighbourhood = range(first_occurance - size, first_occurance + size * 8)
    sample_size = 100
    mean = []
    std = []
    for i in neighbourhood:
        sample = [kolmo(10000, i) for n in range(sample_size)]
        mean.append(np.mean(sample))
        std.append(np.std(sample, ddof=1))
    mean = np.array(mean)
    std = np.array(std)

    #plt.boxplot(data, labels=neighbourhood)
    #plt.plot(list(neighbourhood), [K_alpha(a) for n in neighbourhood], 'm-', label="K_alpha")

    plt.plot(neighbourhood, mean)
    plt.fill_between(
        neighbourhood,
        mean + std,
        mean - std,
        color="r",
        alpha=0.3,
        interpolate=True,
        label="Ein-Sigma-Schlauch"
    )
    plt.plot(neighbourhood, [K_alpha(a)] * len(neighbourhood), 'm', label="K-alpha")

    plt.xlabel("Erwartungswert")
    plt.ylabel("K-S-Wert")
    plt.legend(loc='best')
    plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
    plt.savefig("alpha = " + str(a) + ".pdf")
    plt.clf()
