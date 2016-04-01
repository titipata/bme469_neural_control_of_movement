import numpy as np


def compute_grad(X, y, theta):
    """
    Compute gradient
    """
    m = len(X)
    theta_grad = np.zeros_like(theta)
    for i in range(0, X.shape[1]):
        theta_grad[i] = (1./(m))*np.sum((X.dot(theta) - y)*X[:, i])
    return theta_grad


def compute_cost(X, y, theta):
    """
    Compute cost function
    """
    m = len(X)
    J = (1./(2*m))*np.sum((X.dot(theta) - y)**2, axis=0)
    return J


def sample(X, y, n_sample=20):
    """
    Randomly pick datapoints (to find gradient)
    so called Stochastic gradient descent
    """
    m = len(X)
    idx_sample = np.random.randint(m, size=n_sample)
    return X[idx_sample], y[idx_sample]


if __name__ == '__main__':
    data = np.genfromtxt("data.csv", delimiter=",") # read csv file (don't forget to download!)
    X = data[:,0]
    m = len(X)
    X = np.vstack((np.ones(m), X)).T
    y = data[:,1]
    J = [] # history of cost
    theta = np.array([0, -1]) # intial theta
    n_iter = 3000 # number of iteration
    alpha = 0.0002 # learning rate
    for i in range(n_iter):
        # X_sample, y_sample = sample(X, y)
        theta_grad = compute_grad(X, y, theta)
        theta = theta - alpha*theta_grad
        J.append(compute_cost(X, y, theta))
    print 'learning rate = %s' % alpha
    print 'final theta = %s' % theta
    print 'final cost = %s' % J[-1]
