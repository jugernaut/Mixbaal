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

def fillGrammMatrix(G, line, rbf, dt, vel, D):
    N = line.N()
    NI = line.NI()
    x = line.x()
    
# ----- Wl matrix
    for j in range(N):
        for i in range(NI):
            G[i,j] = rbf.mq(x[i], x[j]) + \
                    dt * ( vel * rbf.d1x(x[i], x[j]) - \
                           D * rbf.d2x(x[i], x[j]) )
# ----- Wb matrix
    for j in range(N):
        for i in range(NI,N):
            G[i,j] = rbf.mq(x[i], x[j])
            
max_iter = 500
dt = 0.002
D = 0.001
vel = 0.1
N = 10
L = 2.5
linea = kn.Line(N, L)
linea.homogeneous()    


print(linea.N(), linea.NB(), linea.NI(), linea.L())
print(linea.x())

G = np.eye(N)
print(G)

u = np.zeros(N)
lam = np.zeros(N)

# Boundary conditions
u[linea.NI()] = 1.0
u[N-1] = 0.0

print(u, lam)

rbf = RBF.Multiquadric(1.0/np.sqrt(N))
print(rbf.mq(1,2), rbf.d1x(1,2), rbf.d2x(1,2), rbf.c())
    
fillGrammMatrix(G, linea, rbf, dt, vel, D)

print(G)

for i in range(1,5):
    print(i)
    lam = np.linalg.solve(G,u)
    u = RBF.evaluate(linea, lam, rbf)
    print(lam)

plt.plot(linea.x(),u,'s')
plt.show()
