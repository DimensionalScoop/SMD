#Berechnung des Medians der Botzmanverteilung:
#Idee: Zunächst Substitution um Problem auf einfachere Form zu bringen
#Dann numerische Integration per Simpsonrgel auf N Intervalle.
#Schränke mit binärer Suche die obere Grenze des Integrals so ein, dass man die gewünschte Wahrscheinlichkeit erhält.

import numpy as np

def f(x):
    return np.exp(-x**2)*x**2

def Simpsonregel(a,b,N):
    h = (b-a)/N
    wert = 0

    for i in range(N):
        tmp = h/6 * ( f(a + i*h) + 4*f( 0.5*((a + i*h) + (a + (i+1)*h)) ) + f(a+(i+1)*h) )
        wert = tmp + wert

    return wert

#print(Simpsonregel(0,5,1000))

#x1 = anfangswet, x2=endwert, x3 Mitte ges=gesuchterwert
ges = np.sqrt(np.pi)/8
x1=0
x2 = 100
N=15000
def intervall(x1,x2,ges):
    x3 = (x1+x2)/2
    med = Simpsonregel(0,x3,N)
    if abs(med - ges) < 0.000000001:
        return x3
    elif med < ges:
        return intervall(x3,x2,ges)
    elif med > ges:
        return intervall(x1,x3,ges)

ergebnis = intervall(x1,x2,ges)
print(ergebnis)
print(Simpsonregel(0,ergebnis,15000))
