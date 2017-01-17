import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib as mpl
import math
import scipy
from scipy import optimize


# c)


# a) und b) und c)

def f(Lambda):
    return (3*Lambda -30*np.log(Lambda) + np.log(math.factorial(13)) + np.log(math.factorial(9))+ np.log(math.factorial(8)))

x = np.linspace(0.000001,80,10000)
plt.plot(x, f(x), 'g-', label=r'$-ln(L)$')
plt.axvline(10, linestyle = '--', color = 'r', label =r'$\lambda_{min}$')
plt.axhline(f(10)+1/2, linestyle = '--', color = 'b', label =r'$-ln(L_{max})+\frac{1}{2}$')
plt.axhline(f(10)+2, linestyle = '--', color = 'y', label =r'$-ln(L_{max})+2$')
plt.axhline(f(10)+9/2, linestyle = '--', color = 'm', label =r'$-ln(L_{max})+\frac{9}{2}$')
#plt.axvspan()
#plt.ylim(-100,200)
#plt.xlabel(r'$\lambda$')
#plt.ylabel(r'$-ln(L)$')
#plt.title(r'negative log-likelihoodfunction')
#plt.legend(loc='best')
#plt.savefig('aufgabe1a.pdf')
#plt.clf()

print("lambda_max =",10)
print("\n")

# c)

def g(Lambda, a):
    return (3*Lambda - 30*np.log(Lambda) - 30 + 30*np.log(10) - a)

def dg(Lambda):
    return (3 - 30/Lambda)

def h(a,x0):
    return (scipy.optimize.newton((lambda Lambda: g(Lambda,a)),x0, dg, maxiter=10000))

interval1 = np.array([h(1/2, 9.5), h(1/2,10.5)])
interval2 = np.array([h(2, 5), h(2, 15)])
interval3 = np.array([h(9/2, 5), h(9/2, 25)])

plt.axvspan(interval1[0], interval1[1], alpha = 0.5, color = 'b')
plt.axvspan(interval2[0], interval1[0], alpha = 0.5, color = 'y')
plt.axvspan(interval1[1], interval2[1], alpha = 0.5, color = 'y')
plt.axvspan(interval3[0], interval2[0], alpha = 0.5, color = 'm')
plt.axvspan(interval2[1], interval3[1], alpha = 0.5, color = 'm')

plt.ylim(-100,200)
plt.xlabel(r'$\lambda$')
plt.ylabel(r'$-ln(L)$')
plt.title(r'negative log-likelihoodfunction')
plt.legend(loc='best')
plt.savefig('aufgabe1a.pdf')
plt.clf()

print("values for non-taylored-version (tol=1.48e-08):")
print("1/2: lambda = ",interval1)
print("intervallength = ",interval1[1]-interval1[0])
print("2: lambda = ",interval2)
print("intervallength = ",interval2[1]-interval2[0])
print("9/2: lambda = ",interval3)
print("intervallength = ",interval3[1]-interval3[0])
print("\n")
# d)

def T_2(Lambda):
    return (30 - 30*np.log(10) + np.log(math.factorial(13)) + np.log(math.factorial(9))+ np.log(math.factorial(8)) + 3/20*(Lambda-10)**2)

x = np.linspace(0.000001,80,10000)
plt.plot(x, f(x), 'k-', label=r'$-ln(L)$')
plt.axvline(10, linestyle = '--', color = 'r', label =r'$\lambda_{min}$')
plt.plot(x, T_2(x), 'g-', label=r'$T_2(30,-ln(L))$')
plt.axhline(T_2(10)+1/2, linestyle = '--', color = 'b', label =r'$T_2(\lambda_{max})+\frac{1}{2}$')
plt.axhline(T_2(10)+2, linestyle = '--', color = 'y', label =r'$T_2(\lambda_{max})+2$')
plt.axhline(T_2(10)+9/2, linestyle = '--', color = 'm', label =r'$T_2(\lambda_{max})+\frac{9}{2}$')
#plt.axvspan()
#plt.ylim(-100,200)
#plt.xlabel(r'$\lambda$')
#plt.ylabel(r'$values$')
#plt.title(r'negative log-likelihoodfunction and taylored-version')
#plt.legend(loc='best')
#plt.savefig('aufgabe1d.pdf')
#plt.clf()

def k(Lambda, a):
    return (3/20 * (Lambda-10)**2 -a)

def dk(Lambda):
    return 6/20*(Lambda-10)

def p(a,x0):
    return (scipy.optimize.newton((lambda Lambda: k(Lambda,a)),x0, dk, maxiter=10000))

t_interval1 = np.array([p(1/2, 9.5), p(1/2,10.5)])
t_interval2 = np.array([p(2, 5), p(2, 15)])
t_interval3 = np.array([p(9/2, 5), p(9/2, 15)])

plt.axvspan(t_interval1[0], t_interval1[1], alpha = 0.5, color = 'b')
plt.axvspan(t_interval2[0], t_interval1[0], alpha = 0.5, color = 'y')
plt.axvspan(t_interval1[1], t_interval2[1], alpha = 0.5, color = 'y')
plt.axvspan(t_interval3[0], t_interval2[0], alpha = 0.5, color = 'm')
plt.axvspan(t_interval2[1], t_interval3[1], alpha = 0.5, color = 'm')

plt.ylim(-100,200)
plt.xlabel(r'$\lambda$')
plt.ylabel(r'$values$')
plt.title(r'negative log-likelihoodfunction and taylored-version')
plt.legend(loc='best')
plt.savefig('aufgabe1d.pdf')
plt.clf()

print("values for taylored-version:")
print("1/2: lambda = ",t_interval1)
print("intervallength = ",t_interval1[1]-t_interval1[0])
print("2: lambda = ",t_interval2)
print("intervallength = ",t_interval2[1]-t_interval2[0])
print("9/2: lambda = ",t_interval3)
print("intervallength = ",t_interval3[1]-t_interval3[0])
print("\n")

print("deviation to exact result:")
print("1/2 :",abs(interval1[0]-interval1[1]-t_interval1[0]+t_interval1[1])/(interval1[1]-interval1[0]) * 100,"%")
print("2 :",abs(interval2[0]-interval2[1]-t_interval2[0]+t_interval2[1])/(interval2[1]-interval2[0]) * 100,"%")
print("9/2 :",abs(interval3[0]-interval3[1]-t_interval3[0]+t_interval3[1])/(interval3[1]-interval3[0]) * 100,"%")
