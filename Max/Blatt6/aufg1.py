import numpy as np
import ROOT
import smd
import pyximport
pyximport.install()
import distance
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def euclidean(a, b):
    """Calculates euclidean distance between 2 a,b vectors.
    """
    return np.linalg.norm(a - b)


def count_occurences(lst):
    """counts occurrences of values in lst"""
    unique, counts = np.unique(lst, return_counts=True)
    return dict(zip(unique, counts))


def most_common_element(lst):
    unique, counts = np.unique(lst, return_counts=True)
    return unique[np.argsort(counts)[-1]]


def kNN(train, train_label, unknown, k):
    """Determines and returns the labels of 'unknown' with the k nearest neighbors algorithm.

    Yields labels.

    Arguments:
            train {numpy array of float tuples} -- training vectors
            train_label {numpy array of any data type} -- classifies training vectors
            unknown {numpy array of float tuples} -- data to classify using 'train'
            k {int} -- number of nearest neighbors to consider
    """

    assert k >= 0
    assert len(train) > 0
    assert len(train_label) == len(train)
    assert len(train) <= 10000  # distance.distances is limited to 10000 values

    for i, vector in enumerate(unknown):
        # calculate distance squared using cython
        dist = distance.distances(train - vector, len(train))[:len(train)]

        nearest = np.argsort(dist)[:k]
        label = most_common_element(train_label[nearest])  # XXX: what happens when k is even and there are the same number of neighbors of two classes?
        yield label


# Stole code reading root files from Jean-Marco because getting data from root files in python still makes me cringe. Every time I try to read the root documentation I wake up on the floor two hours later, curled up into a fetal position, my eyes still burning and the floor wet with tears.
# Sorry.
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


def sample_vector(size, data, start=0):
    # if start == None:
    #     start = np.random.randint(0, len(data[0]) - size)

    stop = start + size
    return np.array((data[0][start:stop], data[1][start:stop], data[2][start:stop])).T


training_size = 5000  # 5000x signal + 5000x background
training_data = np.vstack((sample_vector(training_size, background), sample_vector(training_size, signal)))
# labels are 1 for signal and -1 for background
training_labels = np.hstack((-np.ones(training_size), np.ones(training_size)))

# remove data used for training
background = background[:, training_size:]
signal = signal[:, training_size:]

test_signal_size = 10000
test_background_size = 20000
test_data = np.vstack((sample_vector(test_background_size, background), sample_vector(test_signal_size, signal)))
test_labels = np.hstack((-np.ones(test_background_size), np.ones(test_signal_size)))


def kNN_sliced(unknown):
    return np.array(list(kNN(training_data, training_labels, unknown, 10)))


def analyze(calculated_lables):
    # labels are 1 for signal and -1 for background
    result = test_labels + calculated_lables * 2
    bincount = count_occurences(result)
    assert len(bincount.keys()) <= 4

    true_positive = bincount[3]
    true_negative = bincount[-3]
    false_positive = bincount[1]
    false_negative = bincount[-1]

    print("Reinheit:", true_positive / (true_positive + false_positive))
    print("Effizienz:", true_positive / (true_positive + false_negative))
    print("Genauigkeit:", (true_positive + true_negative) / (true_positive + true_negative + false_positive + false_negative))
    print("Signifikanz:", (true_positive + false_positive) / np.sqrt(true_positive + true_negative + false_positive + false_negative))

print("Calculating kNN, this may take <30s")
calculated_lables = smd.parallel_slice(kNN_sliced, test_data)
analyze(calculated_lables)

plot = False
if plot:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(np.log(test_data[:, 0]), test_data[:, 1], test_data[:, 2], c=test_labels)
    # plt.scatter(test_data[:, 0], test_data[:, 1], c=test_labels)
    plt.show()
