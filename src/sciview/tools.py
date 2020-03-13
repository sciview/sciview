import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize, LogNorm


def edges_to_centers(x):
    """
    Convert array edges to centers
    """
    return 0.5 * (x[1:] + x[:-1])


def centers_to_edges(x):
    """
    Convert array centers to edges
    """
    e = edges_to_centers(x)
    return np.concatenate([[2.0 * x[0] - e[0]], e, [2.0 * x[-1] - e[-1]]])

def get_cmap(data=None, cmap="viridis", log=False, vmin=None, vmax=None):
    """
    Get normalized colormap
    """
    if vmin is None:
        vmin = np.amin(data)
    if vmax is None:
        vmax = np.amax(data)
    if log:
        norm = LogNorm(vmin=10.0**vmin, vmax=10.0**vmax)
    else:
        norm = Normalize(vmin=vmin, vmax=vmax)

    return cm.ScalarMappable(cmap=cmap, norm=norm)
