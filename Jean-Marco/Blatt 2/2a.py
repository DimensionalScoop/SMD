import ROOT
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class random_lcd:

    def __init__(self,a,b,m,x0):
        self.__a=a
        self.__b=b
        self.__m=m
        self.__x=x0

    def random_int(self):
        self.__x = (self.__a * self.__x + self.__b)%(self.__m)
        return self.__x
    def random_float(self):
        self.__x = (self.__a * self.__x + self.__b)%(self.__m)
        return self.__x/self.__m

canvas = ROOT.TCanvas("canvas", "Aufgabe 2a")

random1=random_lcd(1601,3456,10000,0)
random2=random_lcd(1601,3456,10000,100)
random3=random_lcd(1601,3456,10000,500)
random4=random_lcd(1601,3456,10000,1500)
random5=random_lcd(1601,3456,10000,5000)
random6=random_lcd(1601,3456,10000,10000)

a1 = []
for i in range(10000):
    a1.append(random1.random_float())

a2 = []
for i in range(10000):
    a2.append(random2.random_float())

a3 = []
for i in range(10000):
    a3.append(random3.random_float())

a4 = []
for i in range(10000):
    a4.append(random4.random_float())

a5 = []
for i in range(10000):
    a5.append(random5.random_float())

a6 = []
for i in range(10000):
    a6.append(random6.random_float())

canvas.Divide(3,2)

canvas.cd(1)
h1 = ROOT.TH1D("zufall1", "Zufallszahlen, Startwert = 0", 30, min(a1), max(a1))
for tmp in a1:
    h1.Fill(tmp)
h1.Draw()

canvas.cd(2)
h2 = ROOT.TH1D("zufall2", "Zufallszahlen, Startwert = 100", 30, min(a2), max(a2))
for tmp in a2:
    h2.Fill(tmp)
h2.Draw()

canvas.cd(3)
h3 = ROOT.TH1D("zufall3", "Zufallszahlen, Startwert = 500", 30, min(a3), max(a3))
for tmp in a3:
    h3.Fill(tmp)
h3.Draw()

canvas.cd(4)
h4 = ROOT.TH1D("zufall4", "Zufallszahlen, Startwert = 1500", 30, min(a4), max(a4))
for tmp in a4:
    h4.Fill(tmp)
h4.Draw()

canvas.cd(5)
h5 = ROOT.TH1D("zufall5", "Zufallszahlen, Startwert = 5000", 30, min(a5), max(a5))
for tmp in a5:
    h5.Fill(tmp)
h5.Draw()

canvas.cd(6)
h6 = ROOT.TH1D("zufall6", "Zufallszahlen, Startwert = 10000", 30, min(a6), max(a6))
for tmp in a6:
    h6.Fill(tmp)
h6.Draw()

canvas.Print("2b_1.pdf")
