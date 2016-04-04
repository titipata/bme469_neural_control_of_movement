import numpy as np

def update(X, centers):
    # assign cluster and update
    K = len(centers) # number of cluster
    D = np.vstack([np.linalg.norm(X - center, axis=1) for center in centers]) # distance
    clusters = np.argmax(D, axis=0) # find clusters
    centers = np.vstack([X[clusters==k].mean(axis=0) for k in range(K)])

    # compute cost
    J = np.sum([np.sum(np.linalg.norm(X[clusters==k] - centers[k], axis=1)) for k in range(K)])
    return centers, J


def random_centers(X, K):
    """
    Randomly generate K centers from data X
    """
    X_min = X.min(axis=0)
    X_max = X.max(axis=0)
    centers = []
    for k in range(K):
        center = [np.random.uniform(X_min[i], X_max[i]) for i in range(len(X_min))]
        centers.append(center)
    return np.array(centers)


if __name__ == '__main__':
    n_random = 50 # random initialize k-mean multiple time
    n_iter = 100
    K = 2 # number of clusters
    X = np.random.randn(100, 2)*0.3
    X1 = X + [5,3]
    X2 = X + [7,2]
    X = np.vstack((X1,X2))

    output = []
    for n in range(n_random):
        centers = random_centers(X, K)
        J_iter = []
        for i in range(n_iter):
            centers, J = update(X, centers)
            J_iter.append(J)
        output.append([J_iter[-1], centers])

    sel = output[np.argmin([o[0] for o in output])]
    print 'cost = %s' % sel[0]
    print 'final center = %s' % sel[1]
