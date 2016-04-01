import numpy as np


def rbf_kernel(x, y, gamma=0.5):
    """
    Compute radial basis kernel of two vector
    k(x, y) = exp(-gamma*||x-y||^2)
    """
    return np.exp(-gamma*np.linalg.norm(x - y)**2)


def sigmoid_kernel(x, y, gamma=0.5, c0=0):
    """
    Compute sigmiod kernel
    k(x, y) = tanh(-gamma x.T*y + c0)
    """
    return np.tanh(-gamma*np.dot(x, y) + c0)


def laplacian_kernel(x, y, gamma=0.5):
    """
    Compute Laplacian kernel
    k(x, y) = exp(-gamma*||x-y||_1)
    """
    return np.exp(-gamma*nnp.linalg.norm(x - y))


def compute_kernel(X, Y):
    """
    Compute Kernel matrix of data X and Y
    (not efficient, but easy to read)
    """
    K = np.zeros((X.shape[0], Y.shape[0]))
    for i in range(len(X)):
        for j in range(len(Y)):
            K[i, j] = rbf_kernel(X[i], Y[j])
    return K
