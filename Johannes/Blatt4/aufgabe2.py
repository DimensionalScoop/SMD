import ROOT
import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D


# reading data

my_file = ROOT.TFile("zwei_populationen.root","READ")

Tree_2 = my_file.Get("P_0_10000")
Tree_3 = my_file.Get("P_1")

x1_val = np.zeros(1, dtype=float)
y1_val = np.zeros(1, dtype=float)
x2_val = np.zeros(1, dtype=float)
y2_val = np.zeros(1, dtype=float)

Tree_2.SetBranchAddress("x", x1_val)
Tree_2.SetBranchAddress("y", y1_val)
Tree_3.SetBranchAddress("x", x2_val)
Tree_3.SetBranchAddress("y", y2_val)

nentries = Tree_2.GetEntries()

x1 = np.zeros(nentries, dtype=float)
y1 = np.zeros(nentries, dtype=float)
x2 = np.zeros(nentries, dtype=float)
y2 = np.zeros(nentries, dtype=float)

for i in range(nentries):
    Tree_2.GetEntry(i)
    x1[i] = x1_val
    y1[i] = y1_val
    Tree_3.GetEntry(i)
    x2[i] = x2_val
    y2[i] = y2_val

my_file.Close()


# a)

## functions
def g1(x):
    return x*0
def g2(x):
    return -(3/4)*x
def g3(x):
    return -(5/4)*x

## plotting functions and populations
x = np.linspace(-15, 20, 10000)
plt.plot(x , g1(x), 'g-', label=r'$g_1$')
plt.plot(x , g2(x), 'g-', label=r'$g_2$')
plt.plot(x , g3(x), 'g-', label=r'$g_3$')


plt.plot(x1, y1, 'bo', markersize=1, label=r'$P_0$')
plt.plot(x2, y2, 'ro', markersize=1, label=r'$P_1$')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.title(r'Populations of $P_0$ and $P_1$, and projectories.')
plt.legend(loc='best')

plt.savefig('2a.pdf')


# b)

## initialization
### projecting the way that p0 is right of p1
g1_proj = np.array([-1,0])
g2_proj = np.array([-4,3])*1/5
g3_proj = np.array([-4,5])*1/np.sqrt(41)
p0_proj_g1 = []
p1_proj_g1 = []
p0_proj_g2 = []
p1_proj_g2 = []
p0_proj_g3 = []
p1_proj_g3 = []


## calculating projections
for i in range(len(x1)):
    p0_proj = x1[i]*g1_proj[0]+y1[i]*g1_proj[1]
    p0_proj_g1.append(p0_proj)
    p1_proj = x2[i]*g1_proj[0]+y2[i]*g1_proj[1]
    p1_proj_g1.append(p1_proj)

    p0_proj = x1[i]*g2_proj[0]+y1[i]*g2_proj[1]
    p0_proj_g2.append(p0_proj)
    p1_proj = x2[i]*g2_proj[0]+y2[i]*g2_proj[1]
    p1_proj_g2.append(p1_proj)

    p0_proj = x1[i]*g1_proj[0]+y1[i]*g3_proj[1]
    p0_proj_g3.append(p0_proj)
    p1_proj = x2[i]*g1_proj[0]+y2[i]*g3_proj[1]
    p1_proj_g3.append(p1_proj)

## converting to np.arrays
p0_proj_g1 = np.array(p0_proj_g1)
p1_proj_g1 = np.array(p1_proj_g1)

p0_proj_g2 = np.array(p0_proj_g2)
p1_proj_g2 = np.array(p1_proj_g2)

p0_proj_g3 = np.array(p0_proj_g3)
p1_proj_g3 = np.array(p1_proj_g3)

## plotting
plt.plot(p0_proj_g1, g1(p0_proj_g1), 'bo', markersize=1)
plt.plot(p1_proj_g1, g1(p1_proj_g1), 'ro', markersize=1)

plt.plot(p0_proj_g2, g2(p0_proj_g2), 'bo', markersize=1)
plt.plot(p1_proj_g2, g2(p1_proj_g2), 'ro', markersize=1)

plt.plot(p0_proj_g3, g3(p0_proj_g3), 'bo', markersize=1)
plt.plot(p1_proj_g3, g3(p1_proj_g3), 'ro', markersize=1)

plt.savefig('2b.pdf')
plt.clf()

## generating histograms of the different projections
plt.hist(p0_proj_g1, bins=50, alpha=0.5, facecolor='blue', label=r'$P_0$')
plt.hist(p1_proj_g1, bins=50, alpha=0.5, facecolor='red', label=r'$P_1$')
plt.xlabel('projection')
plt.title(r'Projection of $P_0$ and $P_1$ onto $g_1$.')
plt.legend()
plt.savefig('2b1.pdf')
plt.clf()

plt.hist(p0_proj_g2, bins=50, alpha=0.5, facecolor='blue', label=r'$P_0$')
plt.hist(p1_proj_g2, bins=50, alpha=0.5, facecolor='red', label=r'$P_1$')
plt.xlabel('projection')
plt.title(r'Projection of $P_0$ and $P_1$ onto $g_2$.')
plt.legend()
plt.savefig('2b2.pdf')
plt.clf()

plt.hist(p0_proj_g3, bins=50, alpha=0.5, facecolor='blue', label=r'$P_0$')
plt.hist(p1_proj_g3, bins=50, alpha=0.5, facecolor='red', label=r'$P_1$')
plt.xlabel('projection')
plt.title(r'Projection of $P_0$ and $P_1$ onto $g_3$.')
plt.legend()
plt.savefig('2b3.pdf')
plt.clf()

# c)

## functions for one x_cut
def recall_1(x_cut,p0_proj):
    a = len(p0_proj[np.where(p0_proj>x_cut)])
    b = len(p0_proj[np.where(p0_proj<x_cut)])
    return (a/(a+b))

def precision_1(x_cut,p0_proj,p1_proj):
    a = len(p0_proj[np.where(p0_proj>x_cut)])
    b = len(p1_proj[np.where(p1_proj>x_cut)])
    return (a/(a+b))

## functions for all x_cut
def recall(x_cut,p0_proj):
    recall1 = []
    for i in x:
        recall1.append(recall_1(i,p0_proj))
    return np.array(recall1)

def precision(x_cut,p0_proj,p1_proj):
    precision1 = []
    for i in x:
        precision1.append(precision_1(i,p0_proj,p1_proj))
    return np.array(precision1)


## plotting of e and p concerning g1
x = np.linspace(-20,10,10000)
plt.plot(x, recall(x,p0_proj_g1), 'r-', label=r'recall')
plt.plot(x, precision(x,p0_proj_g1,p1_proj_g1), 'b-', label=r'precision')
plt.xlabel(r'$x_{cut}$')
plt.title(r'Recall and precision of $g_1(x_{cut}).$')
plt.legend()
plt.savefig('2c1.pdf')
plt.clf()

## plotting of e and p concerning g2
x = np.linspace(-20,6,10000)
plt.plot(x, recall(x,p0_proj_g2), 'r-', label=r'recall')
plt.plot(x, precision(x,p0_proj_g2,p1_proj_g2), 'b-', label=r'precision')
plt.xlabel(r'$x_{cut}$')
plt.title(r'Recall and precision of $g_2(x_{cut})$.')
plt.legend()
plt.savefig('2c2.pdf')
plt.clf()

## plotting of e and p concerning g3
x = np.linspace(-20,9,10000)
plt.plot(x, recall(x,p0_proj_g3), 'r-', label=r'recall')
plt.plot(x, precision(x,p0_proj_g3,p1_proj_g3), 'b-', label=r'precision')
plt.xlabel(r'$x_{cut}$')
plt.title(r'Recall and precision of $g_3(x_{cut})$.')
plt.legend()
plt.savefig('2c3.pdf')
plt.clf()
