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






    # # x_grid, y_grid = np.meshgrid((x - xmin) * scale_x, (y - ymin) * scale_y, indexing="ij")
    # y_grid, x_grid = np.meshgrid((y - ymin) * scale_y, (x - xmin) * scale_x, indexing="ij")

    # pixel_size_x = (xe[1] - xe[0]) * scale_x
    # pixel_size_y = (ye[1] - ye[0]) * scale_y

    # pts = np.zeros([N, 3], dtype=np.float32)
    # pts[:, 0] = x_grid.flatten()
    # pts[:, 1] = y_grid.flatten()






    # pts = p3.BufferAttribute(array=det_pos)

    scalar_map = get_cmap(data=None, cmap="viridis", log=False, vmin=None, vmax=None)
    colors = scalar_map.to_rgba(data).astype(np.float32)

    # colors = p3.BufferAttribute(
    #     array=scalar_map.to_rgba(data).astype(np.float32))

    nx = xe.shape[0] - 1
    ny = ye.shape[0] - 1
    npixels = nx * ny


    arr_x = np.zeros(2 * nx, dtype=np.float32)
    arr_x[::2] = xe[:-1]
    arr_x[1::2] = xe[1:]
    arr_y = np.zeros(2 * ny, dtype=np.float32)
    arr_y[::2] = ye[:-1]
    arr_y[1::2] = ye[1:]

    x_grid, y_grid = np.meshgrid((arr_x - xmin) * scale_x, (arr_y - ymin) * scale_y)
    # x_grid, y_grid = np.meshgrid(arr_x, arr_y)

    # print(arr_x.dtype)
    # print(x_grid.dtype, y_grid.dtype)
    # print(x_grid.ravel().dtype)
    vertices = np.array([x_grid.ravel(), y_grid.ravel(), np.zeros(x_grid.size, dtype=np.float32)]).T
    del x_grid, y_grid

    face_elem = np.array([[0, 1, nx*2], [1, nx*2+1, nx*2]], dtype=np.uint32)

    # faces = np.tile

    # self.vertices = np.tile(detector_shape, [self.ndets, 1]) + np.repeat(self.det_pos, self.nverts, axis=0)

    # faces = np.arange(self.nverts * self.ndets, dtype=np.uint)
    faces = np.tile(face_elem, [npixels, 1]) + \
            np.repeat(np.arange(0, npixels*2, 2, dtype=np.uint32), 2*3, axis=0).reshape(npixels*2, 3) + \
            np.repeat(np.arange(0, (nx*2)*ny, nx*2, dtype=np.uint32), (nx*2)*3, axis=0).reshape(npixels*2, 3)


    # faces = np.tile(detector_faces, [self.ndets, 1]) + np.repeat(
    #     np.arange(0, self.ndets*self.nverts, self.nverts, dtype=np.uint32), self.nfaces*3, axis=0).reshape(self.nfaces*self.ndets, 3)

    # vertexcolors = np.repeat(colors[:, :3], 4, axis=0).astype(np.float32)

    vertexcolors = np.zeros([2*nx, 2*ny, 3], dtype=np.float32)
    # print(np.shape(vertexcolors))
    # print(np.shape(vertexcolors[::2, ::2, :]))
    # print(np.shape(colors[:, :, :3]))
    vertexcolors[::2, ::2, :] = colors[:, :, :3]
    vertexcolors[1::2, 1::2, :] = colors[:, :, :3]
    vertexcolors[1::2, ::2, :] = colors[:, :, :3]
    vertexcolors[::2, 1::2, :] = colors[:, :, :3]
    # arr_y = np.zeros(2 * ny, dtype=np.float32)
    # arr_y[::2] = ye[:-1]
    # arr_y[1::2] = ye[1:]
    del colors

    # vertexcolors = np.zeros([npixels*2, 3], dtype=np.float32)

    # print(vertices.shape)
    # print(faces.shape)
    # print(vertexcolors.shape)
    # print(vertices.dtype)
    # print(faces.dtype)
    # print(vertexcolors.dtype)

    # print("vertices")
    # print(vertices)
    # print("faces")
    # print(faces)
    # print("colors")
    # print(vertexcolors)
    # print(colors)


    geometry = p3.BufferGeometry(attributes=dict(
        position=p3.BufferAttribute(vertices, normalized=False),
        index=p3.BufferAttribute(faces.ravel(), normalized=False),
        color=p3.BufferAttribute(vertexcolors.reshape(4*nx*ny, 3, order='F')),
    ))


    material = p3.MeshBasicMaterial(vertexColors='VertexColors')
    # material = p3.MeshBasicMaterial()

    # self.material = self.p3.MeshPhongMaterial(vertexColors='VertexColors',
    #                                           transparent=True)


    image = p3.Mesh(geometry=geometry, material=material)







    # geometry = p3.BufferGeometry(attributes={
    #     'position': p3.BufferAttribute(array=pts),
    #     'color': p3.BufferAttribute(
    #         array=scalar_map.to_rgba(data).astype(np.float32))
    # })
    # material = p3.PointsMaterial(vertexColors='VertexColors',
    #                                        size=pixel_size_x)
    #                                        # map=texture,
    #                                        # depthTest=False,
    #                                        # transparent=True)
    # image = p3.Points(geometry=geometry, material=material)





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
    # camera = p3.PerspectiveCamera(position=[0.5*dx, 0.5*dy, 0.5*dx],
    #                                         aspect=dx / dy)
    # camera = p3.PerspectiveCamera(45, dx/dy, 1, 5000)
    camera = p3.OrthographicCamera(0, dx, dy, 0, 0.5*dx, -0.5*dx)

    return render(objects=image, camera=camera,
                  enableRotate=True, width=dx, height=dy)

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
