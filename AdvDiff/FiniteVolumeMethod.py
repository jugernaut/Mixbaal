#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 13:21:50 2018

@author: luiggi
"""

from Mesh import Mesh
from Diffusion import Diffusion1D
from Advection import Advection1D
from Matrix import Matrix

    
if __name__ == '__main__':
    
    m = Mesh(nodes = 5)
    d = Diffusion1D(m.volumes())
    ma = Matrix(m.volumes())
    
    print(m.delta(), d.aP(), ma.mat(), sep='\n')

