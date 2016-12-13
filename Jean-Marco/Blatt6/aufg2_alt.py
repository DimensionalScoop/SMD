import numpy as np

def softmax(G, x, i):
    f = np.matmul(G,x)
    summe = np.sum(f)
    return f[i]/summe

def grad_c(G, x, label):
    ret = np.ones([np.shape(x)[1]])
    for k in range(np.shape(x)[1]):
        for i in range(len(label)):
            ret[k] = ret[k] + softmax(G, x[i], k) - ( k == label[i] )
    ret = ret/len(label)
    return ret

def grad_c_w(G, x, label):
    grad = grad_c(G,x, label)
    summe = np.zeros([np.shape(x)[1], np.shape(x)[1]])
    for i in range(len(x)):
        summe = summe + np.outer(grad, x[i])
    return summe

def grad_c_b(G, x, label):
    grad = grad_c(G,x, label)
    summe = np.zeros([np.shape(x)[1]])
    for i in range(len(x)):
        summe = summe + grad
    return summe

P0 = np.transpose(np.load('P0.npy'))
P1 = np.transpose(np.load('P1.npy'))
Pges = np.append(P0, P1, axis=0)
label = np.append(np.zeros(len(P0)), np.ones(len(P1)))
G = np.random.randn(2,2)
b = np.random.randn(2)
for i in range(5):
    G = G - 0.5 *(grad_c_w(G, Pges, label))
    b = b - 0.5 *(grad_c_w(G, Pges, label))

print(G)
