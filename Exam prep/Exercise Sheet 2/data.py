import numpy


# Produces a toy dataset for testing
def toy(M, N, d):
    U = numpy.random.RandomState(123).uniform(0, 1, [M, d])  # test points (M x d) matrix, with 123 as seed for random number generator. Each row is a test point (d-dimensional vector) and there are M test points.
    X = numpy.random.RandomState(456).uniform(0, 1, [N, d])  # training points (N x d) matrix, with 456 as seed for random number generator. Each row is a training point (d-dimensional vector) and there are N training points.
    Y = numpy.random.RandomState(789).randint(0, 2, [N])  # training labels (N x 1) vector, with 789 as seed for random number generator. Each entry is a label (0 or 1) and there are N labels.
    return U, X, Y


# A small handwritten digits dataset
def digits():
    from sklearn.datasets import load_digits

    d = load_digits()
    R = numpy.random.RandomState(159).permutation(len(d.data))
    return d.data[R] * 1, d.target[R] * 1
