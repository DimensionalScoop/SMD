import numpy as np
import numpy.linalg as linalg
from scipy.linalg import expm
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import math
from matplotlib.patches import Arc


def enable_tex_for_plotting():
    """Set up pyplot for LaTeX"""
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')


def gauss(x, σ, μ):
    """Return Gaussian pdf"""
    return np.exp(-1 / 2 * (x - μ)**2 / σ**2) / np.sqrt(2 * np.pi * σ**2)


def variance_gauss(σ, μ):
    """Return variance of Gaussian"""
    variance, error = integrate.quad(lambda x: (x - μ)**2 * gauss(x, σ, μ), -np.inf, np.inf)

    assert error < 1e-7
    return variance


def gauss_multivariate_prefactor(Σ):
    dim = Σ.size
    return 1 / np.sqrt((2 * np.pi)**dim * linalg.det(Σ))


def gauss_multivariate(x, Σ, μ):
    x = np.array(x)
    μ = np.array(μ)
    dim = x.size
    assert μ.size == dim
    assert Σ.shape == (dim, dim)

    N = gauss_multivariate_prefactor(Σ)
    exp = -1 / 2 * np.dot(np.dot((x - μ).T, linalg.inv(Σ)), (x - μ))

    result = N * np.exp(exp)
    assert np.size(result) == 1
    return result


def rot_matrix_2D(θ):
    """Return rotation matrix for angle θ"""
    rot = ((np.cos(θ), -np.sin(θ)), (np.sin(θ), np.cos(θ)))
    return np.array(rot)


def rotate(M, θ):
    """Rotate matrix M by θ"""
    rot = rot_matrix_2D(θ)
    return np.dot(np.dot(linalg.inv(np.array(rot)), M), np.array(rot))
