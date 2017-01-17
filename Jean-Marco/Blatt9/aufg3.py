
# coding: utf-8

# In[11]:

import numpy as np
import pandas as pd
from numpy.linalg import inv
import matplotlib.pyplot as plt
from scipy import stats

### aufgabe 3a)
print("\nAufgabe 3a:")
def f_fit(a, x):
    summe = 0
    for i, item in enumerate(a):
        summe = summe + item*x**i
    return summe

data = pd.read_csv('aufg_a.csv')
x = data.values.T[0, :]
y = data.values.T[1, :]

A = np.matrix([x**0, x, x**2, x**3, x**4, x**5, x**6]).T #designmatrix
print("Designmatrix:")
print(A, "\n\n")

aTa_trans_inv = inv(np.matmul(A.T, A))

aTa_trans_inv_aT = np.matmul(aTa_trans_inv, A.T)

a = np.ravel(np.matmul(aTa_trans_inv_aT, y)) #ravel to make a 1-dim array
print("Koeffizienten:")
print(a, "\n\n")

val = np.linspace(0, 8, 1000)
plt.plot(val, f_fit(a,val))
plt.plot(x,y, 'k.')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.savefig('3a.pdf')
plt.clf()

### aufgabe 3b)
### nach Skript, Seite 92
print("Aufgabe 3b: \n")
# i dont really understand this C-matrix
C = np.matrix( [[-1, 1, 0, 0, 0, 0, 0, 0],
                [1, -2, 1, 0, 0, 0, 0, 0],
                [0, 1, -2, 1, 0, 0, 0, 0],
                [0, 0, 1, -2, 1, 0, 0, 0],
                [0, 0, 0, 1, -2, 1, 0, 0],
                [0, 0, 0, 0, 1, -2, 1, 0],
                [0, 0, 0, 0, 0, 1, -2, 1],
                [0, 0, 0, 0, 0, 0, 1, -1]] )

a_list = []
lambd_val = [0, 0.1, 0.3, 0.7, 3, 10]
for lambd in lambd_val:
    mat1 = np.matmul(C, A)
    mat2 = np.matmul(A.T, A) + lambd * np.matmul(mat1.T, mat1)
    mat3 = np.matmul(inv(mat2), A.T)
    a = np.matmul(mat3, y)
    a_list.append(np.ravel(a))

val = np.linspace(0, 8, 1000)
for i, args in enumerate(a_list):
    plt.plot(val, f_fit(args,val), label=lambd_val[i])
    print("Lambda = ", lambd_val[i], ":\n ", args)

plt.plot(x,y, 'k.')
plt.legend()
plt.legend(loc='best')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.savefig('3b.pdf')
plt.clf()

### aufgabe 3c)

print("Aufgabe 3c: \n")

data_neu = pd.read_csv('aufg_c.csv')
x = data_neu.values[:,0]
y_means = np.array([])
#x_stds = np.array([])
y_SE = np.array([])

for i, args in enumerate(x):
    y_means = np.append(y_means, np.mean(data_neu.values[i,1:]) )
    #x_stds = np.append(x_stds, np.std(data_neu.values[i,1:]) ) stats.sem does the same job (dont forget *1/sqrt(n) here)
    y_SE = np.append(y_SE, stats.sem(data_neu.values[i,1:]) )

W = np.diag(1/y_SE**2)
print("Gewichtsmatrix W:")
print(W, "\n\n")

mat1 = np.matmul(A.T, W)
mat2 = np.matmul(mat1, A)
mat3 = np.matmul(inv(mat2), A.T)
mat4 = np.matmul(mat3, W)
a = np.ravel(np.matmul(mat4, y))
print("Gewichte:")
print(a)
val = np.linspace(0, 8, 1000)
plt.plot(val, f_fit(a,val))
#plt.plot(x,y_means, 'k.')
plt.errorbar(x, y_means, xerr=0, yerr=y_SE, fmt='k.')
plt.savefig('3c.pdf')
plt.clf()
