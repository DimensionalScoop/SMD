import ROOT
import numpy as np
a,b = np.genfromtxt("Groesse_Gewicht.txt", unpack=True)
canvas = ROOT.TCanvas("canvas", "Aufgabe 2a - Gewichte")
canvas.Divide(3,2)
print(np.std(b))
canvas.cd(1)
h = ROOT.TH1D("Gewicht", "Gewicht, bins=5", 5, min(a), max(a))
for tmp in a:
    h.Fill(tmp)
h.Draw()

canvas.cd(2)
h2 = ROOT.TH1D("Gewicht2", "Gewicht, bins=10", 10, min(a), max(a))
for tmp in a:
    h2.Fill(tmp)
h2.Draw()

canvas.cd(3)
h3 = ROOT.TH1D("Gewicht3", "Gewicht, bins=15", 15, min(a), max(a))
for tmp in a:
    h3.Fill(tmp)
h3.Draw()

canvas.cd(4)
h4 = ROOT.TH1D("Gewicht4", "Gewicht, bins=20", 20, min(a), max(a))
for tmp in a:
    h4.Fill(tmp)
h4.Draw()

canvas.cd(5)
h5 = ROOT.TH1D("Gewicht5", "Gewicht, bins=30", 30, min(a), max(a))
for tmp in a:
    h5.Fill(tmp)
h5.Draw()

canvas.cd(6)
h6 = ROOT.TH1D("Gewicht6", "Gewicht, bins=50", 50, min(a), max(a))
for tmp in a:
    h6.Fill(tmp)
h6.Draw()

canvas.Print("2a_gew.pdf")


### Teil 2

canvas2 = ROOT.TCanvas("canvas2", "Aufgabe 2b - Groessen")
canvas2.Divide(3,2)

canvas2.cd(1)
hh = ROOT.TH1D("Groesse", "Groesse, bins=5", 5, min(b), max(b))
for tmp in b:
    hh.Fill(tmp)
hh.Draw()

canvas2.cd(2)
hh2 = ROOT.TH1D("Groesse2", "Groesse, bins=10", 10, min(b), max(b))
for tmp in b:
    hh2.Fill(tmp)
hh2.Draw()

canvas2.cd(3)
hh3 = ROOT.TH1D("Groesse3", "Groesse, bins=15", 15, min(b), max(b))
for tmp in b:
    hh3.Fill(tmp)
hh3.Draw()

canvas2.cd(4)
hh4 = ROOT.TH1D("Groesse4", "Groesse, bins=20", 20, min(b), max(b))
for tmp in b:
    hh4.Fill(tmp)
hh4.Draw()

canvas2.cd(5)
hh5 = ROOT.TH1D("Groesse5", "Groesse, bins=30", 30, min(b), max(b))
for tmp in b:
    hh5.Fill(tmp)
hh5.Draw()

canvas2.cd(6)
hh6 = ROOT.TH1D("Groesse6", "Groesse, bins=50", 50, min(b), max(b))
for tmp in b:
    hh6.Fill(tmp)
hh6.Draw()

canvas2.Print("2a_groesse.pdf")
