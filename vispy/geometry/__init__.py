# -*- coding: utf-8 -*-
# Copyright (c) 2014, Vispy Development Team.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

"""
This module implements classes and methods for handling geometric data.
"""

from __future__ import division

__all__ = ['MeshData', 'PolygonData', 'Rect', 'Triangulation', 'triangulate',
           'create_arrow', 'create_cone', 'create_cube', 'create_cylinder',
           'create_sphere', 'resize']

from .polygon import PolygonData  # noqa
from .meshdata import MeshData  # noqa
from .rect import Rect  # noqa
from .triangulation import Triangulation, triangulate  # noqa
from .torusknot import TorusKnot  # noqa
from .calculations import (_calculate_normals, _fast_cross_3d,  # noqa
                           resize)  # noqa
from .generation import (create_arrow, create_box, create_cone,  # noqa
                         create_cube, create_cylinder, create_plane,  # noqa
                         create_sphere)  # noqa
