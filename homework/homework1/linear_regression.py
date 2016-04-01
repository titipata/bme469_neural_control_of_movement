import numpy as np


def compute_grad(X, y, theta):
    """
    Compute gradient
    """
    m = len(X)
    theta_grad = np.array([0, 0])
    for i in range(m):
        theta_grad[0] += (1./(m))*((theta[0] + theta[1]*X[i]) - y[i])
        theta_grad[1] += (1./(m))*((theta[0] + theta[1]*X[i]) - y[i])*X[i]
    return theta_grad

def compute_cost(X, y, theta):
    """
    Compute cost function
    """
    m = len(X)
    J = 0
    for i in range(m):
        J += (1./(2*m))*((theta[0] + theta[1]*X[i]) - y[i])**2
    return J


def sample(X, y, n_sample=20):
    """
    Randomly pick datapoints (to find gradient)
    so called Stochastic gradient descent
    """
    idx_sample = np.random.randint(m,size=n_sample)
    return X[idx_sample], y[idx_sample]


if __name__ == '__main__':
    data = np.genfromtxt("data.csv", delimiter=",") # read csv file (don't forget to download!)
    X = data[:,0]
    y = data[:,1]
    J = [] # history of cost
    theta = np.array([0, -1]) # intial theta
    n_iter = 3000 # number of iteration
    alpha = 0.0001 # learning rate
    for i in range(n_iter):
        X_sample, y_sample = sample(X, y)
        theta_grad = compute_grad(X_sample, y_sample, theta)
        theta = theta - alpha*theta_grad
        J.append(compute_cost(X, y, theta))
    print 'learning rate = %s' % alpha
    print 'final theta = %s' % theta
    print 'final cost = %s' % J[-1]
