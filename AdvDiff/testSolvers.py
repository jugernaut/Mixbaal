#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 11:58:12 2018

@author: luiggi
"""

import numpy as np
import StationarySolvers as sol
import KrylovSolvers as kry

import time
    
def generateSystem(Nx, Ny, diagonal):
    N = Nx * Ny
    A = np.zeros((N,N))

# Primero llena los bloques tridiagonales
    for j in range(0,Ny):
        ofs = Nx * j
        A[ofs, ofs] = diagonal; 
        A[ofs, ofs + 1] = 1
        for i in range(1,Nx-1):
            A[ofs + i, ofs + i]     = diagonal
            A[ofs + i, ofs + i + 1] = 1
            A[ofs + i, ofs + i - 1] = 1
            A[ofs + Nx - 1, ofs + Nx - 2] = 1; 
            A[ofs + Nx - 1, ofs + Nx - 1] = diagonal 

# Despues llena las dos diagonales externas
    for k in range(0,N-Nx):
        A[k, Nx + k] = 1
        A[Nx + k, k] = 1

    boundA = 100
    boundB = -25
    boundC = 34
    boundD = 7

    f = np.zeros((Ny,Nx)) # RHS
# Aplicacion de las condiciones de frontera Dirichlet
    f[0   ,:] -= boundA # Bottom wall    
    f[Ny-1,:] -= boundB # Upper wall
    f[:,0   ] -= boundC # Left wall 
    f[:,Nx-1] -= boundD # Right wall
    f.shape = f.size     # Cambiamos los arreglos a formato unidimensional

    return A, f

Nx = 10
Ny = 10
A, b = generateSystem(Nx, Ny,-4) # Matriz del sistema

tol = 1e-6
max_iter = 100
w = 1.5

t1 = time.clock()
ut = np.linalg.solve(A,b)
t2 = time.clock()
te = t2 - t1
print("\n linalg.solve() \n Elapsed time to solve Ax = b : %g" % te)

t1 = time.clock()
ut,error,it = sol.jacobi(A,b,tol,max_iter)
t2 = time.clock()
te = t2 - t1
print("\n Jacobi \n Elapsed time to solve Ax = b : %g" % te)
print(" error : %g, iteraciones : %d" % (error, it))

t1 = time.clock()
ut,error,it = sol.gauss_seidel(A,b,tol,max_iter)
t2 = time.clock()
te = t2 - t1
print("\n Gauss Seidel \n Elapsed time to solve Ax = b : %g" % te)
print(" error : %g, iteraciones : %d" % (error, it))

t1 = time.clock()
ut,error,it = sol.sor(A,b,tol,max_iter,w)
t2 = time.clock()
te = t2 - t1
print("\n SOR \n Elapsed time to solve Ax = b : %g" % te)
print(" error : %g, iteraciones : %d" % (error, it))

b = np.matrix(b)
x0 = b.copy()

t1 = time.clock()
ut,residual,it = kry.steepestDescent(A,b.T,x0.T,tol,max_iter)
t2 = time.clock()
te = t2 - t1
print("\n Steepest Descent \n Elapsed time to solve Ax = b : %g" % te)
print(" residual : %g, iteraciones : %d" % (residual, it))
