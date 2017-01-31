import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib as mpl

psi = np.arange(0,360,30)
asy = np.array([-0.032, 0.01, 0.057, 0.068, 0.076, 0.08, 0.031, 0.005, -0.041, -0.090, -0.088, -0.074])

def f_1(psi):
    return np.cos(psi)

def f_2(psi):
    return np.sin(psi)

# a)

design = []
for item in psi:
    design.append([f_1(item), f_2(item)])

# b)

b = np.matmul(np.transpose(design),design)
c = np.linalg.inv(b)
a = np.matmul(c,(np.matmul(np.transpose(design),asy)))
print(a)

# c)

v = np.matmul(c,np.matmul(np.transpose(design),np.var(asy)*np.matmul(design,c)))
print(v)
a1 = np.sqrt(v[0][0])
a2 = np.sqrt(v[1][1])
print("Standardabweichung a1 = ",a1)
print("Standardabweichung a2 = ",a2)
rho = v[0][1]/np.sqrt(v[0][0]*v[1][1])
print("Korrelationskoeffizient =",rho)

# d)

A0 = a[0]*np.sqrt((a[0]/a[1])**2 + 1)
delta = np.arctan(-a[0]/a[1])

def f(x):
    return A0*np.cos(x+delta)

print(A0)
print(delta)

print(asy-f(psi))
