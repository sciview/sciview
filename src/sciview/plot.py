# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (c) 2020 Sciview contributors (https://github.com/sciview)
# @file
# @author Neil Vaytet

from .plot_1d import plot_1d

def plot(*args,
         **kwargs):
    """
    Wrapper function to plot any kind of dataset
    """

    return plot_1d(*args, **kwargs)
