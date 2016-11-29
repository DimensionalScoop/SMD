import ROOT
import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

# reading data

my_file = ROOT.TFile("zwei_populationen.root", "READ")

Tree_2 = my_file.Get("P_0_10000")
Tree_3 = my_file.Get("P_1")

x1_val = np.zeros(1, dtype=float)
y1_val = np.zeros(1, dtype=float)
x2_val = np.zeros(1, dtype=float)
y2_val = np.zeros(1, dtype=float)

Tree_2.SetBranchAddress("x", x1_val)
Tree_2.SetBranchAddress("y", y1_val)
Tree_3.SetBranchAddress("x", x2_val)
Tree_3.SetBranchAddress("y", y2_val)

nentries = Tree_2.GetEntries()

x1 = np.zeros(nentries, dtype=float)
y1 = np.zeros(nentries, dtype=float)
x2 = np.zeros(nentries, dtype=float)
y2 = np.zeros(nentries, dtype=float)

for i in range(nentries):
    Tree_2.GetEntry(i)
    x1[i] = x1_val
    y1[i] = y1_val
    Tree_3.GetEntry(i)
    x2[i] = x2_val
    y2[i] = y2_val

my_file.Close()
