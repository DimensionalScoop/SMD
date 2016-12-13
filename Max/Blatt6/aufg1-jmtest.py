import numpy as np
from numpy import linalg as LA
import ROOT


def TreeToArray(tree, branchname, size_to_get, datatype=float):
    '''Gets an tree, puts the values from branchname to an array. Datatype float/int, etc'''
    nentries = tree.GetEntries()
    assert size_to_get <= nentries
    x = np.zeros(size_to_get, dtype=datatype)
    x_val = np.zeros(1, dtype=datatype)
    tree.SetBranchAddress(branchname, x_val)
    for i in range(size_to_get):
        tree.GetEntry(i)
        x[i] = x_val
    return x

root_file = ROOT.TFile("NeutrinoMC.root")
tree0 = root_file.Get("Signal_MC_Akzeptanz")
tree1 = root_file.Get("Untergrund_MC")

sample_size = 20000 + 5000 + 2

x_sig = TreeToArray(tree0, "x", sample_size)
y_sig = TreeToArray(tree0, "y", sample_size)
hits_sig = TreeToArray(tree0, "AnzahlHits", sample_size)
signal = np.array((hits_sig, x_sig, y_sig))

x_u = TreeToArray(tree1, "x", sample_size)
y_u = TreeToArray(tree1, "y", sample_size)
hits_u = TreeToArray(tree1, "AnzahlHits", sample_size)
background = np.array((hits_u, x_u, y_u))
print("Completed reading data")

sig_val = np.stack((x_sig, y_sig, hits_sig), axis=-1)
u_val = np.stack((x_u, y_u, hits_u), axis=-1)  # get an array where every entry is an array containing the attributes

train_val = np.append(sig_val[np.random.randint(len(sig_val), size=10000)], u_val[np.random.randint(len(u_val), size=20000)], axis=0)  # put together 30000 random entriess
train_label = np.append(np.ones(10000, int), np.zeros(20000, int))

test_val = np.append(sig_val[np.random.randint(len(sig_val), size=5000)], u_val[np.random.randint(len(u_val), size=5000)], axis=0)  # put together 5000 random entries
test_label = np.append(np.ones(5000, int), np.zeros(5000, int))


def dist(train, tbk):
    return LA.norm(train - tbk, axis=-1)


def kNN(train, lable, tbk, k):
    '''k-nearest-neighbors-algorithmn.
    args:
        train: array with arrays of the attributes of the train-data
        lable: array with lables of test-data. attributes should be integeres or bool
        tbk: attributes of the test sample we want to classify
        k: k nearest neighbors'''
    diff = dist(train, tbk)
    index = np.argsort(diff) <= k  # index of k smallest distances
    counts = np.bincount(lable[index])
    return np.argmax(counts)  # returns the most common lable


results = np.array([], int)
for i in test_val:
    results = np.append(results, kNN(train_val, train_label, i, 10))

tp = sum(np.equal(results[results > 0], test_label[results > 0]))
fp = sum(np.not_equal(results[results > 0], test_label[results > 0]))
fn = sum(np.not_equal(results[results < 1], test_label[results < 1]))
tn = sum(np.equal(results[results < 1], test_label[results < 1]))

print("Reinheit", tp / (tp + fp))
print("Effizient", tp / (tp + fn))
print("Signifikanz", (tp + fp) / np.sqrt(tp + fp + fn + tn))
