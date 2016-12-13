import numpy as np
import matplotlib.pyplot as plt


def softmax(G, x, a , b):
    '''softmax-function.
    args:
        G: weight-matrix
        x: array with koordinates of one point
        a: class
        b: biasvector'''
    f = np.matmul(G,x) + b
    summe = np.sum(np.exp(f))
    return np.exp(f[a])/summe

def grad_c_w(G, x, label, i, b):
    '''W-gradient of c concerning one point.
    args:
        G: weight-matrix
        x: array with koordinates of one point
        label: array containing labels of the populations
        i: index of one point
        b: biasvector'''
    grad = np.zeros(G.shape[0])
    for k in range(G.shape[1]):
        grad[k] = softmax(G, x[i], k, b) - int(label[i] == k)
    return np.outer(grad, x[i])

def grad_c_b(G, x, label, i, b):
    '''b-gradient of c concerning one point.
    args:
        G: weight-matrix
        x: array with koordinates of one point
        label: array containing labels of the populations
        i: index of one point
        b: biasvector'''
    grad = np.zeros(b.shape[0])
    for k in range(b.shape[0]):
        grad[k] = softmax(G, x[i], k, b) - int(label[i] == k)
    return grad

def grad_ges(G, x, label, b):
    '''Sum of all W-gradients of c concerning one point.
    args:
        G: weight-matrix
        x: array with koordinates of one point
        label: array containing labels of the populations
        i: index of one point
        b: biasvector'''
    summe = np.zeros(G.shape)
    for i in range(len(x)):
        summe = summe + grad_c_w(G, x, label, i, b)
    summe = summe * 1/len(x)
    return summe

def b_ges(G, x, label, b):
    '''Sum of all b-gradients of c concerning one point.
    args:
        G: weight-matrix
        x: array with koordinates of one point
        label: array containing labels of the populations
        i: index of one point
        b: biasvector'''
    summe = np.zeros(b.shape)
    for i in range(len(x)):
        summe = summe + grad_c_b(G, x, label, i, b)
    summe = summe * 1/len(x)
    return summe

def slicer_beam(G,x,b):
    '''Slicer Beam returning cut.
    args:
        G: final weight-matrix
        x: array in range of population in x-axis
        b: final biasvector'''
    return (G[0][0]-G[0][1])/(G[1][1]-G[0][1])*x + (b[0]-b[1])/(G[1][1]-G[0][1])

P0 = np.transpose(np.load('P0.npy'))
P1 = np.transpose(np.load('P1.npy'))
Pges = np.append(P0, P1, axis=0)
label = np.append(np.zeros(len(P0)), np.ones(len(P1)))
G = np.array([[0.5,0.5],[0.5,0.5]])
b = np.array([0.5,0.5])
h = 0.5

print("Optimizing parameters ,status:")
for u in range(100):
    print("    ",u,"%")
    tmp1 = grad_ges(G, Pges, label, b)
    tmp2 = b_ges(G, Pges, label, b)
    G = G - h * tmp1
    b = b - h * tmp2

zug = np.array([])
for i in range(len(Pges)):
    zug = np.append(zug, np.argmax(np.matmul(G, Pges[i])+b))
print(np.sum(np.abs(label-zug))/len(Pges)*100, "%"," Fehlerrate")
print("W = ",G)
print("b = ",b)

t = np.arange(20000)
plt.plot(t, zug[t])
plt.savefig('plot.pdf')


plt.clf()

x = np.linspace(-15, 20, 10000)
plt.plot(x , slicer_beam(G,x,b), 'g-', label=r'$slicer beam$')


plt.plot(P0[:,0], P0[:,1], 'b.', markersize=1, label=r'$P_0$')
plt.plot(P1[:,0], P1[:,1], 'r.', markersize=1, label=r'$P_1$')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.title(r'Populations of $P_0$ and $P_1$ with slicer beam.')
plt.legend(loc='best')
plt.savefig('plot1.pdf')
