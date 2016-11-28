import ROOT
import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D


# preparations for d)

my_file = ROOT.TFile("zwei_populationen.root", "RECREATE")

Tree_1 = ROOT.TTree("P_0_1000", "P_0_1000")
fill_me_x3 = np.zeros(1, dtype=float)
fill_me_y3 = np.zeros(1, dtype=float)
Tree_1.Branch('x', fill_me_x3, 'x/D')
Tree_1.Branch('y', fill_me_y3, 'y/D')

Tree_2 = ROOT.TTree("P_0_10000", "P_0_10000")
fill_me_x1 = np.zeros(1, dtype=float)
fill_me_y1 = np.zeros(1, dtype=float)
Tree_2.Branch('x', fill_me_x1, 'x/D')
Tree_2.Branch('y', fill_me_y1, 'y/D')

Tree_3 = ROOT.TTree("P_1", "P_1")
fill_me_x2 = np.zeros(1, dtype=float)
fill_me_y2 = np.zeros(1, dtype=float)
Tree_3.Branch('x', fill_me_x2, 'x/D')
Tree_3.Branch('y', fill_me_y2, 'y/D')



# b)

## initialization
mean1  = [0,3]
rho1   = 0.9
cov1   = rho1*3.5*2.6
covm1  = [[3.5**2,cov1],[cov1,2.6**2]]
mean2  = 6
std2   = 3.5
x1     = []
y1     = []
x2     = []
y2     = []
x_ges  = []
y_ges  = []

## generating values for P_0_10000 and P_1
for i in range(0,10000):
    a = np.random.multivariate_normal(mean1,covm1)
    x1.append(a[0])
    fill_me_x1[0] = a[0]
    y1.append(a[1])
    fill_me_y1[0] = a[1]
    Tree_2.Fill()
    b = np.random.normal(mean2, std2)
    x2.append(b)
    fill_me_x2[0] = b
    c = np.random.normal(0.6*b-0.5, 1)
    y2.append(c)
    fill_me_y2[0] = c
    Tree_3.Fill()

## gaining overall population
x_ges = x1
x_ges.extend(x2)
y_ges = y1
y_ges.extend(y2)


## plotting
plt.plot(x1, y1, 'bo', markersize=1,label=r'$P_0$')
plt.plot(x2, y2, 'ro', markersize=1,label=r'$P_1$')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.title(r'Populations of $P_0$ and $P_1$.')
plt.legend(loc='best')
plt.savefig('fig/1b.pdf')

plt.clf()



#c)

## converting lists to np.arrays
x1 = np.array(x1)
x2 = np.array(x2)
x_ges = np.array(x_ges)
y1 = np.array(y1)
y2 = np.array(y2)
y_ges = np.array(y_ges)

## means
x1_mean_stich = np.mean(x1)
x2_mean_stich = np.mean(x2)
x_ges_mean_stich = np.mean(x_ges)
y1_mean_stich = np.mean(y1)
y2_mean_stich = np.mean(y2)
y_ges_mean_stich = np.mean(y_ges)

## variances
a = np.cov([x1,y1])
b = np.cov([x2,y2])
c = np.cov([x_ges,y_ges])
x1_var_stich = a[0,0]
x2_var_stich = b[0,0]
x_ges_var_stich = c[0,0]
y1_var_stich = a[1,1]
y2_var_stich = b[1,1]
y_ges_var_stich = c[1,1]

## covariances
p1_covar_stich = a[1,0]
p2_covar_stich = b[1,0]
p_ges_covar_stich =c[1,0]

## correlations
p1_cor_stich = a[1,0]/(np.sqrt(a[0,0]*a[1,1]))
p2_cor_stich = b[1,0]/(np.sqrt(b[0,0]*b[1,1]))
p_ges_cor_stich = c[1,0]/(np.sqrt(c[0,0]*c[1,1]))


## printing
print("population0:")
print("mean_x = ", x1_mean_stich)
print("mean_y = ", y1_mean_stich)
print("var_x = ", x1_var_stich)
print("var_y = ", y1_var_stich)
print("covar = ", p1_covar_stich)
print("cor = ", p1_cor_stich)

print("population1:")
print("mean_x = ", x2_mean_stich)
print("mean_y = ", y2_mean_stich)
print("var_x = ", x2_var_stich)
print("var_y = ", y2_var_stich)
print("covar = ", p2_covar_stich)
print("cor = ", p2_cor_stich)

print("both populations:")
print("mean_x = ", x_ges_mean_stich)
print("mean_y = ", y_ges_mean_stich)
print("var_x = ", x_ges_var_stich)
print("var_y = ", y_ges_var_stich)
print("covar = ", p_ges_covar_stich)
print("cor = ", p_ges_cor_stich)


#d)

## initialization
x3 = []
y3 = []

## generating values for P_0_1000
for i in range(0,1000):
    a = np.random.multivariate_normal(mean1,covm1)
    x3.append(a[0])
    fill_me_x3[0] = a[0]
    y3.append(a[1])
    fill_me_y3[0] = a[1]
    Tree_1.Fill()

# closing rootfile

my_file.Write()
my_file.Close()
