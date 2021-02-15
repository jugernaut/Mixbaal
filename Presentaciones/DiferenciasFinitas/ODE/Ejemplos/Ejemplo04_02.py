#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 16:57:20 2017

@author: luiggi
"""
import numpy as np
import pylab as pl      
    
Nt = 10
a = 0
b = 2
t = np.linspace(a,b,Nt)

def sol(t, delta, delta0):
    return (t+1)**2 + (delta + delta0 + 0.5) * np.exp(t) - delta

def error(t,epsilon):
    return (2 * np.exp(t)**2 + 1) * epsilon

# Usar diferentes valores de estas deltas y ver que pasa ...
delta = 1e-01
delta0 = 1e-05

y = sol(t, 0 ,0 )
z = sol(t, delta, delta0)

pl.plot(t,y, 'or-', label='Sol.')
pl.plot(t,z, 'vb-', label='Sol. Per')

# Ver que pasa con diferentes valores de epsilon 
#en = np.abs(y - z)
#ea = error(t,delta)
#pl.plot(t,en, 'g-', label='Error')
#pl.plot(t,ea, 'k-', label='Cota')

pl.xlabel('$t$')
pl.ylabel('$y(t)$')
pl.legend()
pl.grid()
pl.show



