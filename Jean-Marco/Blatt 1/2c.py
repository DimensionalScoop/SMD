import ROOT
import numpy as np
canvas = ROOT.TCanvas("canvas", "Aufgabe 2c - Zufallszahlen")
canvas.Divide(3,2)
zufall = ROOT.TRandom(34123) # Zufallsgenerator mit random seed
a=[]
for i in range(10**5):
    a.append(zufall.Integer(100)+1)


a=np.log(a)
print(a.max)
canvas.cd(1)
h = ROOT.TH1D("Zufall", "Zufall, bins=5", 5, min(a), max(a))
for tmp in a:
    h.Fill(tmp)
h.Draw()

canvas.cd(2)
h2 = ROOT.TH1D("Zufall2", "Zufall, bins=10", 10, min(a), max(a))
for tmp in a:
    h2.Fill(tmp)
h2.Draw()

canvas.cd(3)
h3 = ROOT.TH1D("Zufall3", "Zufall, bins=15", 15, min(a), max(a))
for tmp in a:
    h3.Fill(tmp)
h3.Draw()

canvas.cd(4)
h4 = ROOT.TH1D("Zufall4", "Zufall, bins=20", 20, min(a), max(a))
for tmp in a:
    h4.Fill(tmp)
h4.Draw()

canvas.cd(5)
h5 = ROOT.TH1D("Zufall5", "Zufall, bins=30", 30, min(a), max(a))
for tmp in a:
    h5.Fill(tmp)
h5.Draw()

canvas.cd(6)
h6 = ROOT.TH1D("Zufall6", "Zufall, bins=50", 50, min(a), max(a))
for tmp in a:
    h6.Fill(tmp)
h6.Draw()

canvas.Print("2c.pdf")
