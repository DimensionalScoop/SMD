import numpy as np
import matplotlib.pyplot as plt

def softmax(G, x,a):
    f = np.matmul(G,x)
    summe = np.sum(np.exp(f))
    return np.exp(f[a])/summe

def grad_c_w(G, x, label, i):
    f = np.matmul(G, x[i])
    grad = np.zeros(2)
    for k in range(2):
        grad[k] = softmax(G, x[i], k) - int(label[i] == k)
    return np.outer(grad, x[i])

def grad_c_b(G, x, label, i):
    f = np.matmul(G, x[i])
    grad = np.zeros(2)
    for k in range(2):
        grad[k] = softmax(G, x[i], k) - int(label[i] == k)
    return grad

def grad_ges(G, x, label):
    summe = np.zeros([2,2])
    for i in range(len(x)):
        tmp = grad_c_w(G, x, label, i)
        summe = summe + tmp
    summe = summe * 1/len(x)
    return summe

def b_ges(G, x, label):
    summe = np.zeros(2)
    for i in range(len(x)):
        summe = summe + grad_c_b(G, x, label, i)
    summe = summe * 1/len(x)
    return summe


P0 = np.transpose(np.load('P0.npy'))
P1 = np.transpose(np.load('P1.npy'))
Pges = np.append(P0, P1, axis=0)
label = np.append(np.zeros(len(P0)), np.ones(len(P1)))
G = np.array([[0.5,0.5],[0.5,0.5]])
b = np.array([0.5,0.5])
h = 0.5
for u in range(1):
    tmp = grad_ges(G, Pges, label)
    G = G - h * tmp
    b = b - h * b_ges(G,Pges,label)

zug = np.array([])
for i in range(len(Pges)):
    zug = np.append(zug, np.argmax(np.matmul(G, Pges[i])+b))
print(np.sum(np.abs(label-zug)))
print(G)

t = np.arange(20000)
plt.plot(t, zug[t])
plt.savefig('plot.pdf')
