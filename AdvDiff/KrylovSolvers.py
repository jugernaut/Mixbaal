#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 17:15:18 2018

@author: luiggi
"""

import numpy as np

def steepestDescent(A,b,x0,tol,kmax):    
    r = b - A * x0
    k = 0
    res = np.linalg.norm(r)
#    print(k, res)
    while(res > tol and k < kmax):
        alpha = float(r.T * r) / float(r.T * A * r)
        x0 = x0 + alpha * r
        r = b - A * x0
        res = np.linalg.norm(r)
        k += 1
#        print(k, res)
    return x0, res, k 
        
if __name__ == '__main__':

    tol = 1e-6
    max_iter = 100
    A = np.matrix([[3, 2],[2,6]] )
    b = np.matrix([[2],[-8]])
    x0 = np.matrix([[-2],[-2]])
    
    sol, res, it = steepestDescent(A,b,x0,tol,max_iter)
    print('\n Steepest Descent \n Solucion: {} \n Residual : {} \n Iteraciones : {}'.format(sol.flatten(), res, it))

    