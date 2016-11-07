import numpy as np
import scipy.stats as stats

μ = (4, 2)
σ = (3.5, 1.5)
cov = 4.2

ρ = cov / np.prod(σ)
print("a)", ρ)
