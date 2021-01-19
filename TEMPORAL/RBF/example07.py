#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 20:03:13 2018

@author: luiggi
"""

import numpy as np
import Knots as kn
import RadialBasisFunctions as RBF
import matplotlib.pyplot as plt

def fillGrammMatrix(G, line, rbf, D):
    N = line.N()
    NI = line.NI()
    x = line.x()
    
# ----- WL block matrix
    for i in range(NI):
        for j in range(N):
            G[i,j] = D * rbf.d2x(x[i], x[j])
            
# ----- WB block matrix
    for i in range(NI,N):
        for j in range(N):
            G[i,j] = rbf.mq(x[i], x[j])
            
D = 1.0
N = 11
L = 1.0
linea = kn.Line(N, L)
linea.homogeneous()    

G = np.eye(N)

u = np.zeros(N)
lam = np.zeros(N)

# Boundary conditions
u[linea.NI()] = 1.0
u[-1] = 0.0

rbf = RBF.Multiquadric(1.0/np.sqrt(N))
    
fillGrammMatrix(G, linea, rbf, D)

print(G)

lam = np.linalg.solve(G,u)
print(lam)

u = RBF.evaluate(linea, lam, rbf)

plt.plot(linea.x(),u,'s')
plt.grid()
plt.show()
