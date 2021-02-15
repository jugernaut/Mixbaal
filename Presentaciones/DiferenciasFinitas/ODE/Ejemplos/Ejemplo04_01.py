#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 16:57:20 2017

@author: luiggi
"""
import numpy as np
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D

def grafica3D(t):
    def f(t,y):
        return y - t**2 + 1
    
    Ny = len(t)
    ay = 0.5
    by = 15
    y = np.linspace(ay,by,Ny)
    xg,yg = np.meshgrid(t,y)
    
    tipo = int(input('| Contornos [1] o Superficie [2] '))

    if tipo == 1:
        pl.contourf(xg,yg,f(xg,yg),5,alpha=.75,cmap=pl.cm.hot)
        C = pl.contour(xg,yg,f(xg,yg),5, colors='black', linewidth=.5)
        pl.clabel(C,inline=1,fontsize=10)
        pl.xlabel('$t$')
        pl.ylabel('$y(t)$')
        pl.grid()
        pl.xlim(a - 0.2,b + 0.2)
        pl.ylim(ay - 0.2, by + 0.2)
    else:
        fig = pl.figure()
        ax = Axes3D(fig)
        ax.plot_surface(xg,yg,f(xg,yg), rstride=1, cstride=1, alpha=.85,cmap=pl.cm.hot)
        ax.contour(xg,yg,f(xg,yg),5, colors='black', linewidth=.5)
        ax.set_zlim(-2,15)
        pl.xlabel('$t$')
        pl.ylabel('$y(t)$')
        
    pl.show()
    
Nt = 10
a = 0
b = 2
t = np.linspace(a,b,Nt)

grafica3D(t)




