# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (c) 2020 Scipp contributors (https://github.com/scipp)
# @author Neil Vaytet

from . import config
from .render import render

import pythreejs as p3
# import ipywidgets as widgets
import numpy as np
# import IPython.display as disp

def plot_1d(x, y, color="blue", linewidth=2, background="#DDDDDD"):


    if len(x) != len(y):
        raise RuntimeError("bad shape")

    N = len(x)

    dx = config.figure["width"]
    dy = config.figure["height"]

    xmin = np.amin(x)
    ymin = np.amin(y)

    scale_x = dx / (np.amax(x) - xmin)
    scale_y = dy / (np.amax(y) - ymin)

    pts = np.zeros([N, 3], dtype=np.float32)
    pts[:, 0] = (x - xmin) * scale_x
    pts[:, 1] = (y - ymin) * scale_y
    # arr = p3.BufferAttribute(array=pts)
    geometry = p3.BufferGeometry(attributes={
        'position': p3.BufferAttribute(array=pts),
    })
    material = p3.LineBasicMaterial(color=color, linewidth=linewidth)
    line = p3.Line(geometry=geometry,
                              material=material)
    # width = 800
    # height= 500

    # Create the threejs scene with ambient light and camera
    # camera = p3.PerspectiveCamera(position=[0.5*dx, 0.5*dy, 0],
    #                                         aspect=dx / dy)
    camera = p3.OrthographicCamera(0, dx, dy, 0, 0.5*dx, -0.5*dx)

    return render(objects=line, camera=camera, background=background,
                  enableRotate=False, width=dx, height=dy)

    # # key_light = p3.DirectionalLight(position=[0, 10, 10])
    # # ambient_light = p3.AmbientLight()
    # scene = p3.Scene(children=[line, camera], background="#DDDDDD")
    # controller = p3.OrbitControls(controlling=camera, enableRotate=False)
    # # Render the scene into a widget
    # renderer = p3.Renderer(camera=camera, scene=scene,
    #                                  controls=[controller],
    #                                  width=dx,
    #                                  height=dy)
    # return renderer
