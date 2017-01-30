
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt


#a
def create_matrix(e, n):
    A = np.zeros((n,n))
    for i in range(n):
        if i==0:
            A[0][0] = 1-e
            A[0][1] = e
        elif i==range(n)[-1]:
            A[-1][-1] = 1-e
            A[-1][-2] = e
        else:
            A[i][i-1] = e
            A[i][i] = 1-2*e
            A[i][i+1] = e
    return A


# In[2]:


#b
A = create_matrix(0.23, 20)
f = np.array([193,485,664,763,804,805,779,736,684,626,566,508,452,400,351,308,268,233,202,173])
g = np.matmul(A,f)

g_mess = np.zeros(20)
for i in range(20):
    g_mess[i] = np.random.poisson(g[i])



# In[3]:

print(g)
print(g_mess)


# In[4]:


#c
eigens = np.linalg.eig(A)
D = np.diag(eigens[0])
U = eigens[1]
U_inv = np.linalg.inv(eigens[1])

idx = np.argsort(-eigens[0])
D_sorted = np.diag(eigens[0][idx])
U_sorted = U[:, idx]
U_sorted_inv = np.linalg.inv(U_sorted)


# In[15]:


#d

b = np.matmul(U_sorted_inv, f)
c = np.matmul(U_sorted_inv, g)

V_f = np.diag(f) # Kovarianzmatrix wegen Poission
V_b = np.matmul( U_sorted_inv, np.matmul( V_f, np.transpose(U_sorted_inv) ) )

b_mess = np.matmul(np.linalg.inv(D_sorted), np.matmul(U_sorted_inv, g_mess))

b_mess_norm = b_mess/np.sqrt(np.diagonal(V_b))

plt.plot(range(20), b_mess_norm, 'x')
plt.plot(range(20), np.ones(20))
#plt.plot(range(20), b/np.diagonal(V_b), 'xr')
plt.show()


# In[17]:

print(np.linalg.inv(D_sorted))


# In[11]:

plt.clf()
plt.plot(range(20), b_mess, 'xb')
plt.plot(range(20), b, 'xr')
plt.show()


# In[7]:

plt.clf()
g_mess = np.matmul(U_sorted, b_mess)
plt.errorbar(range(20), g_mess, yerr=np.sqrt(np.diagonal(V_b)), fmt='o')
plt.plot(range(20), g, "xr")
plt.show()


# In[46]:

#e
cutoff = 7

D_sorted_reg = np.copy(D_sorted)
D_sorted_reg_inv = np.linalg.inv(D_sorted_reg)
for i in range(cutoff,20):
    D_sorted_reg_inv[i][i] = 0

b_mess_reg = np.matmul(D_sorted_reg_inv, np.matmul(U_sorted_inv, g_mess))

g_mess_reg = np.matmul(U_sorted, b_mess_reg)

plt.clf()
g_mess = np.matmul(U_sorted, b_mess)
plt.errorbar(range(20), g_mess_reg, yerr=np.sqrt(np.diagonal(V_b)), fmt='o')
plt.plot(range(20), g, "xr")
plt.show()

