import numpy as np
from numpy.linalg import inv

A = np.matrix( [ [1, np.sqrt(3)/2, 1/2, 0, -1/2, -np.sqrt(3)/2, -1, -np.sqrt(3)/2, -1/2, 0, 1/2, np.sqrt(3)/2] , [0, 1/2, np.sqrt(3)/2, 1, np.sqrt(3)/2, 1/2, 0, -1/2, -np.sqrt(3)/2, -1, -np.sqrt(3)/2, -1/2] ] )
A = np.transpose(A)

tmp = np.matmul(np.transpose(A),A)
tmpinv = inv(tmp)
G = tmpinv * np.transpose(A)

y = np.matrix( [-0.032, 0.010, 0.057, 0.068, 0.076, 0.080, 0.031, 0.005, -0.041, -0.09, -0.088, -0.074] )
y = np.transpose(y)
a = G*y
print(a)



### Part 2


V = np.matrix( [ [0.00449**2, 0 ] , [0, 0.00449**2 ] ] )
J = np.matrix( [ [0.43607, -0.89991] , [10.46304, 5.07017] ] )
#J = np.transpose(J)
tmp2 =  np.matmul( V, np.transpose(J))
V_neu = np.matmul( J, tmp2)

print(V_neu)
