#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 07:03:27 2018

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

L = 0.02 # meters
TA = 100  # °C 
TB = 200  # °C 
k  = 0.5  # W/m.K
q  = 1e+06 # 1e+06 W/m^3 = 1000 kW/m^3 Fuente uniforme
N  = 21 # Número de nodos

linea = kn.Line(N, L)
linea.homogeneous()    

G = np.eye(N)

T = np.zeros(N)
f = np.zeros(N)
lam = np.zeros(N)

# Boundary conditions
T[linea.NI()] = TA
T[-1] = TB

f = T - q

print(f)

c = 1.0/np.sqrt(N)
rbf = RBF.Multiquadric(c)
    
fillGrammMatrix(G, linea, rbf, k)

print(G)

lam = np.linalg.solve(G,f)
print(lam)

T = RBF.evaluate(linea, lam, rbf)
x = 100 * linea.x()
plt.plot(x,T,'s')
plt.grid()
plt.show()