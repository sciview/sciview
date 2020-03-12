
from . import config

import pythreejs as p3
import numpy as np

def axes_1d(x, y, color="#000000", linewidth=1.5):

    N = len(x)

    pts = np.zeros([5, 3])

    xmin = np.amin(x)
    xmax = np.amax(x)
    ymin = np.amin(y)
    ymax = np.amax(y)


    pts[:, 0] = x
    pts[:, 1] = y
    geometry = p3.BufferGeometry(attributes={
        'position': p3.BufferAttribute(array=pts),
    })
    material = p3.LineBasicMaterial(color=color, linewidth=linewidth)
    line = p3.Line(geometry=geometry,
                              material=material)
    width = 800
    height= 500
