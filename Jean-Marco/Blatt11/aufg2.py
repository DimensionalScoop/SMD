import numpy as np

def f(e, g1, g2):
    return 5/4 * 1/(1-2*e) * ( (1-e) *g1 - e*g2)

g1 = 200
g2 = 169

print("f1 ", f(0.1, 200, 169 ) )
print("f2 ", f(0.1, 169, 200 ))

def fehler(e, g1, g2):
    return 25/16 * 1/(1-2*e)**2 * ( g1 * (1-e)**2 + e**2 * g2 )

def korr(e, g1, g2):
    return 25/16 * 1/(1-2*e)**2 * ( -e * (1-e) * g1 - e * (1-e) * g2 )

# d

a = fehler(0.1, 169, 200)
b = fehler(0.1, 200, 169)
c = korr(0.1, 200, 169)
print("s1 ", a)
print("s2 ", b)
print("Cov ", c)

print("Korr", c / np.sqrt(a*b))

# e

print("Aufgabe e:")
a = fehler(0.4, 169, 200)
b = fehler(0.4, 200, 169)
c = korr(0.4, 200, 169)
print("s1 ", a)
print("s2 ", b)
print("Cov ", c)

print("Korr", c / np.sqrt(a*b))
