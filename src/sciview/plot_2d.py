# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (c) 2020 Scipp contributors (https://github.com/scipp)
# @author Neil Vaytet

from . import config
from .render import render
from .tools import centers_to_edges, get_cmap

import pythreejs as p3
# import ipywidgets as widgets
import numpy as np
# import IPython.display as disp

def plot_2d(x, y, data, cmap="viridis", vmin=None, vmax=None):


    # if len(x) != len(y):
    #     raise RuntimeError("bad shape")

    N = data.size

    dx = config.figure["width"]
    dy = config.figure["height"]

    xe = centers_to_edges(x)
    ye = centers_to_edges(y)

    xmin = np.amin(xe)
    ymin = np.amin(ye)

    scale_x = dx / (np.amax(xe) - xmin)
    scale_y = dy / (np.amax(ye) - ymin)

    # x_grid, y_grid = np.meshgrid((x - xmin) * scale_x, (y - ymin) * scale_y, indexing="ij")
    y_grid, x_grid = np.meshgrid((y - ymin) * scale_y, (x - xmin) * scale_x, indexing="ij")

    pixel_size_x = (xe[1] - xe[0]) * scale_x
    pixel_size_y = (ye[1] - ye[0]) * scale_y

    pts = np.zeros([N, 3], dtype=np.float32)
    pts[:, 0] = x_grid.flatten()
    pts[:, 1] = y_grid.flatten()

    # pts = p3.BufferAttribute(array=det_pos)

    scalar_map = get_cmap(data=None, cmap="viridis", log=False, vmin=None, vmax=None)
    # colors = scalar_map.to_rgba(data).astype(np.float32)

    # colors = p3.BufferAttribute(
    #     array=scalar_map.to_rgba(data).astype(np.float32))
    geometry = p3.BufferGeometry(attributes={
        'position': p3.BufferAttribute(array=pts),
        'color': p3.BufferAttribute(
            array=scalar_map.to_rgba(data).astype(np.float32))
    })
    material = p3.PointsMaterial(vertexColors='VertexColors',
                                           size=pixel_size_x)
                                           # map=texture,
                                           # depthTest=False,
                                           # transparent=True)
    image = p3.Points(geometry=geometry, material=material)





    # # arr = p3.BufferAttribute(array=pts)
    # geometry = p3.BufferGeometry(attributes={
    #     'position': p3.BufferAttribute(array=pts),
    # })
    # material = p3.LineBasicMaterial(color=color, linewidth=linewidth)
    # line = p3.Line(geometry=geometry,
    #                           material=material)
    # # width = 800
    # # height= 500

    # # Create the threejs scene with ambient light and camera
    # # camera = p3.PerspectiveCamera(position=[0.5*dx, 0.5*dy, 0],
    #                                         aspect=dx / dy)
    camera = p3.OrthographicCamera(0, dx, 0, dy, -0.5*dx, 0.5*dx)

    return render(objects=image, camera=camera,
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
