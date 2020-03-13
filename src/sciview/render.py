# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (c) 2020 Scipp contributors (https://github.com/scipp)
# @author Neil Vaytet

from . import config

import pythreejs as p3


def render(objects=None, camera=None, background="#DDDDDD", enableRotate=True,
           width=0, height=0):

    if isinstance(objects, list):
        children = objects + [camera]
    else:
        try:
            _ = iter(objects)
            children = list(objects) + [camera]
        except TypeError:
            children = [objects, camera]
    scene = p3.Scene(children=children, background=background)
    controller = p3.OrbitControls(controlling=camera, enableRotate=enableRotate)
    # Render the scene into a widget
    renderer = p3.Renderer(camera=camera, scene=scene,
                                     controls=[controller],
                                     width=width,
                                     height=height)
    return renderer
