import numpy as np
import ROOT
from numpy import linalg as LA
import matplotlib.pyplot as plt
#Methoden

def TreeToArray(tree, branchname, datatype=float):
    '''Gets an tree, puts the values from branchname to an array. Datatype float/int, etc'''
    nentries = tree.GetEntries()
    x = np.zeros(nentries, dtype=datatype)
    x_val = np.zeros(1, dtype=datatype)
    tree.SetBranchAddress(branchname, x_val)
    for i in range(nentries):
        tree.GetEntry(i)
        x[i] = x_val
    return x



#Daten Einlesen
root_file = ROOT.TFile("zwei_populationen.root")
tree0 = root_file.Get("P_0_10000")
tree1 = root_file.Get("P_1")

x0 = TreeToArray(tree0, "x")
y0 = TreeToArray(tree0, "y")
x1 = TreeToArray(tree1, "x")
y1 = TreeToArray(tree1, "y")



#Aufgabe a)
x0_mean = np.mean(x0)
y0_mean = np.mean(y0)
x1_mean = np.mean(x1)
y1_mean = np.mean(y1)

print("Mittelwerte P0: x =", x0_mean, ", y =", y0_mean)
print("Mittelwerte P1: x =", x1_mean, ", y =", y1_mean)


#Aufgabe b)
s0 = np.zeros((2,2))
for i in range(len(x0)):
    s0 = s0 + np.outer( (x0[i]-x0_mean,y0[i]-y0_mean) , (x0[i]-x0_mean,y0[i]-y0_mean)  )
s1 = np.zeros((2,2))

for i in range(len(x1)):
    s1 = s1 + np.outer( (x1[i]-x1_mean,y1[i]-y1_mean) , (x1[i]-x1_mean,y1[i]-y1_mean)  )

sb = np.outer( (x0_mean-x1_mean,y0_mean-y1_mean),(x0_mean-x1_mean,y0_mean-y1_mean))

print("S_P0:")
print(s0)
print("S_P1:")
print(s1)
print("S_Pb:")
print(sb)

#Aufgabe c)
sw = s0+s1
sw_inv = LA.inv(sw)
lambd = np.dot(sw_inv, np.array([x0_mean-x1_mean,y0_mean-y1_mean]))
l_norm = lambd / LA.norm(lambd)
print("Lambda:", l_norm)

#Aufgabe d)

project_p0 = []
for i in range(len(x0)):
    project_p0.append( np.dot( (x0[i],y0[i]), l_norm))

project_p1 = []
for i in range(len(x1)):
    project_p1.append( np.dot( (x1[i],y1[i]), l_norm))

plt.hist(project_p0, bins=50, alpha=0.8, label=r"Signal")
plt.hist(project_p1, bins=50, alpha=0.8, label=r"Untergrund")
plt.xlabel(r'$\lambda_{Proj}$')
plt.title(r"Fischer Diskiminanzanalyse")
plt.legend(loc='best')
plt.savefig('fig/1d.pdf')
plt.clf()

#Aufgabe e) / f)
max_lim = np.max([np.max(project_p0), np.max(project_p1)])
min_lim = np.min([np.min(project_p0), np.min(project_p1)])

tp = []
fn = []
fp = []
tn = []
signal = []
untergrund = []
lam_index = []
for i in np.linspace(min_lim, max_lim-0.01, 100):
    tp.append(sum(project_p0>i))
    fn.append(sum(project_p0<i))
    fp.append(sum(project_p1>i))
    tn.append(sum(project_p1<i))
    lam_index.append(i)

tp = np.array(tp)
fn = np.array(fn)
fp = np.array(fp)
tn = np.array(tn)
lam_index = np.array(lam_index)

plt.plot(lam_index, tp/(tp+fn), label=r'Effizienz')
plt.plot(lam_index, tp/(tp+fp), label=r'Reinheit')
plt.xlabel(r'$\lambda_{cut}$')
plt.legend()
plt.legend(loc='best')
plt.savefig('fig/1e.pdf')
plt.clf()


#Aufgabe 1f)
plt.plot(lam_index, (tp)/(fp), label=r'$\frac{S}{B}$')
plt.xlabel(r'$\lambda_{cut}$')
plt.legend()
plt.legend(loc='best')
plt.savefig('fig/1f.pdf')
plt.clf()

#Aufgabe 1g)
plt.plot(lam_index, (tp)/(np.sqrt(tp+fp)), label=r'$\frac{S}{\sqrt{S + B}}$')
plt.xlabel(r'$\lambda_{cut}$')
plt.legend()
plt.legend(loc='best')
plt.savefig('fig/1g.pdf')
plt.clf()
print("Maximale Signifikanz für", lam_index[np.argmax((tp)/(np.sqrt(tp+fp)))])
