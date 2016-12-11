import numpy as np


def euclidean(a, b):
    """Calculates euclidean distance between 2 a,b vectors.
    """
    return np.linalg.norm(a - b)


def kNN(train, train_label, unknown, k, distance=euclidean):
    """Determines and returns the labels of 'unknown' with the k nearest neighbors algorithm.

    Yields labels.

    Arguments:
            train {numpy array of float tuples} -- training vectors
            train_label {numpy array of any data type} -- classifies training vectors
            unknown {numpy array of float tuples} -- data to classify using 'train'
            k {int} -- number of nearest neighbors to consider
            distance {function(vector, vector) returning floats} -- function to determine distance between vectors from 'train' and 'unknown'
    """

    assert k >= 0
    assert len(train) > 0
    assert len(train_label) == len(train)

    for vector in unknown:
        dist = euclidean(vector, train)
        nearest = np.argsort(dist)[:k]
        label = np.argmax(train_label[nearest])

        assert dist[nearest[0]] >= dist[np.argsort(dist)[-1]]
        yield label
