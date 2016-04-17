# utilities file for the project

import neo
import numpy as np

events = {
    'lightsoff': "lights_off",
    'press': "lever_off",
    'pumpon': "reward_on",
    'release': "lever_on",
    'toneon': "tone_on",
}


def read_data(filename):
    if filename.endswith("h5"):
        r = neo.io.NeoHdf5IO(filename=filename)
        seg = r.read_segment()
        r.close()
        return seg, events
    else:
        print "File not H5 or NEX. Returning."
        return None, None


def pca(x, n_components=2):
    """
    reduce dimensions using
    principal components analysis
    """
    x = x - np.mean(x, axis=0)
    u, s, v = np.linalg.svd(x, full_matrices=False)
    # x_pca = x*v = u*s*(v^T*V) = u*s
    x_pca = u[:,:n_components]*s[:n_components]
    return x_pca
