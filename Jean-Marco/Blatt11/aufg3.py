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



#b
A = create_matrix(0.23, 20)
f = np.array([193,485,664,763,804,805,779,736,684,626,566,508,452,400,351,308,268,233,202,173])
g = np.matmul(A,f)

g_mess = np.zeros(20)
for i in range(20):
    g_mess[i] = np.random.poisson(g[i]) # Ermittle die "Zufälligen" Messfehler


print("g ergibt sich zu: ", g, "\n")
print("g_mess ergibt sich zu: ", g_mess, "\n")


#c
eigens = np.linalg.eig(A) # Diagonalisiere die Matrix A
D = np.diag(eigens[0]) # Matrix D enthält Eigenwerte auf Diagonale
U = eigens[1] # Matrix U enthält Eigenvektoren als Spalten
U_inv = np.linalg.inv(eigens[1])

idx = np.argsort(-eigens[0]) # Sortiere die Eigenwerte absteigend!
D_sorted = np.diag(eigens[0][idx]) # Ordne die Eigenwerte in D richtig an
U_sorted = U[:, idx] # Ordne die Eigenvektoren in U richtig an
U_sorted_inv = np.linalg.inv(U_sorted)

#d

b = np.matmul(U_sorted_inv, f) # Ermittle b und c
c = np.matmul(U_sorted_inv, g)

V_f = np.diag(f) # Kovarianzmatrix wegen Poission
V_b = np.matmul( U_sorted_inv, np.matmul( V_f, np.transpose(U_sorted_inv) ) ) # Transformiere mit BVB-Formel

V_g_mess = np.diag(g_mess) # Kovarianzmatrix, wobei diesmal g_mess als Ausgang genommen wird
L = np.matmul(np.linalg.inv(D_sorted), U_sorted_inv) # Matrix L transformiert von g in b, siehe Abgabe
V_b_mess = np.matmul(L, np.matmul(V_g_mess, np.transpose(L))) # Transformiere von g_mess in b_mess mit BVB

b_mess = np.matmul(L, g_mess)

b_mess_norm = b_mess/np.sqrt(np.diagonal(V_b_mess)) # normiere b's auf Standardabweichung

plt.clf()
plt.plot(range(20), b_mess_norm, 'x')
plt.plot(range(-1, 21), np.ones(22))
plt.plot(range(-1, 21), -np.ones(22))
plt.xlim(-1, 20)
plt.xlabel(r'$\mathrm{Index} j$')
plt.ylabel(r'$\frac{b_j}{\sigma_j}$', rotation=0)
plt.savefig('plot3a.pdf')



plt.clf() # Plotte aus Spaß die Koeffizienten b von der "wahren" und der "verfälschten" Messung
plt.xlabel(r'$\mathrm{Index} j$')
plt.ylabel(r'$b_j$', rotation=0)
plt.plot(range(20), b_mess, 'xb', label=r'$b_{mess}$')
plt.plot(range(20), b, 'xr', label=r'$b$')
plt.legend(loc='best')
plt.savefig('plot3b.pdf')

plt.clf()
f_mess = np.matmul(U_sorted, b_mess) # Führe entfaltetes b_mess in richtige Basis zurück
L_ges = np.matmul(U, np.matmul(np.linalg.inv(D_sorted), U_sorted_inv)) # L_ges transformiert von g bis ganz nach f
V_f_mess = np.matmul(L_ges, np.matmul(V_g_mess, np.transpose(L_ges))) # ermittle Kovarianzmatrix von f

plt.xlabel(r'$\mathrm{Index} j$')
plt.ylabel(r'$f$', rotation=0)
plt.errorbar(range(20), f_mess, yerr=np.sqrt(np.diagonal(V_f_mess)), fmt='o')
plt.plot(range(20), f, "xr")
plt.title(r"Entfaltete Werte ohne Regularisierung")
plt.savefig('plot3c.pdf')



#e
cutoff = 8

D_sorted_reg = np.copy(D_sorted)
D_sorted_reg_inv = np.linalg.inv(D_sorted_reg)
for i in range(cutoff,20):
    D_sorted_reg_inv[i][i] = 0 # setze ab Cutoff alle Diagonalelemente von D auf null


b_mess_reg = np.matmul(D_sorted_reg_inv, np.matmul(U_sorted_inv, g_mess)) # entfalte g_mess mit Regularisiertem D

f_mess_reg = np.matmul(U_sorted, b_mess_reg)

L_ges_reg = np.matmul(U, np.matmul(np.linalg.inv(D_sorted_reg), U_sorted_inv)) # L transformiert g in f
V_f_mess_reg = np.matmul(L_ges_reg, np.matmul(V_g_mess, np.transpose(L_ges_reg))) # bestimme Fehler von f

plt.clf()
plt.xlabel(r'$\mathrm{Index} j$')
plt.ylabel(r'$f$', rotation=0)
plt.title(r"Entfaltete Werte mit Cutoff bei j=8")
plt.errorbar(range(20), f_mess_reg, yerr=np.sqrt(np.diagonal(V_b)), fmt='o')
plt.plot(range(20), f, "xr")
plt.savefig('plot3d.pdf')
