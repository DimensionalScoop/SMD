import ROOT
import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D


# reading data

my_file = ROOT.TFile("zwei_populationen.root","READ")

Tree_1 = my_file.Get("P_0_1000")
Tree_2 = my_file.Get("P_0_10000")
Tree_3 = my_file.Get("P_1")

x1_val = np.zeros(1, dtype=float)
y1_val = np.zeros(1, dtype=float)
x2_val = np.zeros(1, dtype=float)
y2_val = np.zeros(1, dtype=float)
x3_val = np.zeros(1, dtype=float)
y3_val = np.zeros(1, dtype=float)


Tree_2.SetBranchAddress("x", x1_val)
Tree_2.SetBranchAddress("y", y1_val)
Tree_3.SetBranchAddress("x", x2_val)
Tree_3.SetBranchAddress("y", y2_val)
Tree_1.SetBranchAddress("x", x3_val)
Tree_1.SetBranchAddress("y", y3_val)

nentries  = Tree_2.GetEntries()
nentries2 = Tree_1.GetEntries()

x1 = np.zeros(nentries, dtype=float)
y1 = np.zeros(nentries, dtype=float)
x2 = np.zeros(nentries, dtype=float)
y2 = np.zeros(nentries, dtype=float)
x3 = np.zeros(nentries2, dtype=float)
y3 = np.zeros(nentries2, dtype=float)

for i in range(nentries):
    Tree_2.GetEntry(i)
    x1[i] = x1_val
    y1[i] = y1_val
    Tree_3.GetEntry(i)
    x2[i] = x2_val
    y2[i] = y2_val

for i in range(nentries2):
    Tree_1.GetEntry(i)
    x3[i] = x3_val
    y3[i] = y3_val

my_file.Close()


# functions

## adjusts coordinates to a population
def ordne(x,y):
    p = []
    for i in range(len(x)):
        v = [x[i],y[i]]
        p.append(v)
    p = np.array(p)
    return p

## calculates 'streumatrizen'
def streu(p,p_mean):
    S = np.zeros(2)
    for i in range(len(p)):
        v1 = p[i]-p_mean
        v1 = np.array(v1)
        v2 = [v1*v1[0],v1*v1[1]]
        v2 = np.array(v2)
        S = S + v2
    return S

## giving linear function to given vector
def g1(x,v):
    return (v[1]/v[0])*x

## functions for one x_cut (super mario copy-pasta)
def recall_1(x_cut,p0_proj):
    a = len(p0_proj[np.where(p0_proj>x_cut)])
    b = len(p0_proj[np.where(p0_proj<x_cut)])
    return (a/(a+b))

def precision_1(x_cut,p0_proj,p1_proj):
    a = len(p0_proj[np.where(p0_proj>x_cut)])
    b = len(p1_proj[np.where(p1_proj>x_cut)])
    return (a/(a+b))

def s_to_b_1(x_cut,p0_proj,p1_proj):
    a = len(p0_proj[np.where(p0_proj>x_cut)])
    b = len(p1_proj[np.where(p1_proj>x_cut)])
    if b == 0:
        return 0
    return (a/b)

def significance_1(x_cut,p0_proj,p1_proj):
    a = len(p0_proj[np.where(p0_proj>x_cut)])
    b = len(p1_proj[np.where(p1_proj>x_cut)])
    return (a/np.sqrt(a+b))

## functions for all x_cut
def recall(x_cut,p0_proj):
    recall1 = []
    for i in x_cut:
        recall1.append(recall_1(i,p0_proj))
    return np.array(recall1)

def precision(x_cut,p0_proj,p1_proj):
    precision1 = []
    for i in x_cut:
        precision1.append(precision_1(i,p0_proj,p1_proj))
    return np.array(precision1)

def s_to_b(x_cut,p0_proj,p1_proj):
    s_to_b1 = []
    for i in x_cut:
        s_to_b1.append(s_to_b_1(i,p0_proj,p1_proj))
    return np.array(s_to_b1)

def significance(x_cut,p0_proj,p1_proj):
    significance1 = []
    for i in x_cut:
        significance1.append(significance_1(i,p0_proj,p1_proj))
    return np.array(significance1)



## function answering d) to g), generated due to h), v is the normalized 'fischer'-vector
##### in der Aufgabenstellung steht schließlich, dass wir nur e) bis g) wiederholen sollen, nur jetzt aber die Population auswechseln
def d_bis_g(v, x1, x2, y1, y2, plot1, plot2, plot3, plot4, plot5, plot6,k):
    ## projecting
    p0_proj = v[0]*x1+v[1]*y1
    p1_proj = v[0]*x2+v[1]*y2
    ##################################################### testing
    x = np.linspace(-15, 20, 10000)
    plt.plot(x , g1(x,v), 'g-', label=r'$g_1$')


    plt.plot(x1, y1, 'bo', markersize=1, label=r'$P_0$')
    plt.plot(x2, y2, 'ro', markersize=1, label=r'$P_1$')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.title(r'Populations of $P_0$ and $P_1$, and projectories.'+k)
    plt.legend(loc='best')

    plt.savefig('fig/'+plot1, format='pdf')


    plt.plot(p0_proj, g1(p0_proj,v), 'bo', markersize=1)
    plt.plot(p1_proj, g1(p1_proj,v), 'ro', markersize=1)


    plt.savefig('fig/'+plot2, format='pdf')
    plt.clf()
    #########################################################

    ## plotting histogram
    plt.hist(p0_proj, bins=50, alpha=0.5, facecolor='blue', label=r'$P_0$')
    plt.hist(p1_proj, bins=50, alpha=0.5, facecolor='red', label=r'$P_1$')
    plt.xlabel('projection')
    plt.title(r'Projection of $P_0$ and $P_1$.'+k)
    plt.legend()
    plt.savefig('fig/'+plot3, format='pdf')
    plt.clf()


    # e)

    ## calculating precision and recall of this projection
    x = np.linspace(-15,10,10000)
    plt.plot(x, recall(x,p0_proj), 'r-', label=r'recall')
    plt.plot(x, precision(x,p0_proj,p1_proj), 'b-', label=r'precision')
    plt.xlabel(r'$x_{cut}$')
    plt.title(r'Recall and precision of $g_1(x_{cut}).$'+k)
    plt.legend()
    plt.savefig('fig/'+plot4, format='pdf')
    plt.clf()

    # g)

    ## plotting proportion and gaining max
    ## only using proportions in range with p1
    a = x[np.where(s_to_b(x,p0_proj,p1_proj) == np.amax(s_to_b(x,p0_proj,p1_proj)))]
    print(k+" Proportion at max at x = ",a)
    plt.plot(x, s_to_b(x,p0_proj,p1_proj), 'b-', label=r'$\frac{S}{B}$')
    #plt.axvline(a)
    plt.xlabel(r'$x_{cut}$')
    plt.title(r'Proportion'+k)
    plt.legend()
    plt.savefig('fig/'+plot5, format='pdf')
    plt.clf()

    ## plotting significance and gaining max
    a = x[np.where(significance(x,p0_proj,p1_proj) == np.amax(significance(x,p0_proj,p1_proj)))]
    print(k+" Significance at max at x = ",a)
    plt.plot(x, significance(x,p0_proj,p1_proj), 'b-', label=r'$\frac{S}{\sqrt{S+B}}$')
    plt.xlabel(r'$x_{cut}$')
    plt.title(r'Significance'+k)
    plt.legend()
    plt.savefig('fig/'+plot6, format='pdf')
    plt.clf()
    return

#a)

## generating populations
p0 = ordne(x1,y1)
p1 = ordne(x2,y2)
## calculating 'mean'-vectors
p0_mean = np.array([np.mean(x1),np.mean(y1)])
p1_mean = np.array([np.mean(x2),np.mean(y2)])

# b)

## calculating matrices
s0_streu = streu(p0,p0_mean)
s1_streu = streu(p1,p1_mean)
## calculating sw
sw = s0_streu + s1_streu
## inverting sw
sw_inv = np.linalg.inv(sw)
## calculating sb
sb = np.array([(p0_mean-p1_mean)*(p0_mean-p1_mean)[0],(p0_mean-p1_mean)*(p0_mean-p1_mean)[1]])
## matix needed for calculation of eigenvectors
sw_inv_sb = sw_inv*sb
# c)

## calculating eigenvectors
w, v = np.linalg.eig(sw_inv_sb)

## choosing the eigenvector with the highest eigenvalue
#v = v[0]
#lambda_fischer = np.copy(v)
#print(lambda_fischer)
lambda_fischer = np.dot(sw_inv, p0_mean-p1_mean)
v = np.copy(lambda_fischer)

## normalizing
a = np.linalg.norm(v)
v = v/a
print("Values of the 'fischer'-vektor:")
print("lambda = ",a)
print("e_lambda = ", v)

## p0 should be right of p1 (cosmetics)
v = -v

# d)
print("Data for P_0_10000:")
d_bis_g(v,x1, x2, y1, y2, 'test1','test2','1d','1e','1f','1g',' (P_0_10000)')

# h)
print("Data for P_0_1000:")
d_bis_g(v,x3, x2, y3, y2, 'test1_h','test2_h','1h_d','1h_e','1h_f','1h_g',' (P_0_1000)')
