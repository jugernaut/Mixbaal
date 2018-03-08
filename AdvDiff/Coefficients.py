#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 15:11:05 2018

@author: luiggi
"""

import numpy as np

class Coefficients():
    
    def __init__(self, nvx = None):
        self.__nvx = nvx
        self.__aP = np.zeros(nvx)
        self.__aE = np.zeros(nvx)
        self.__aW = np.zeros(nvx)
        self.__Su = np.zeros(nvx)
    
    def __del__(self):
        del(self.__aP)
        del(self.__aE)
        del(self.__aW)
        del(self.__Su)
        
    def aP(self):
        return self.__aP

    def aE(self):
        return self.__aE
    
    def aW(self):
        return self.__aW
    
    def Su(self):
        return self.__Su

    def bcDirichlet(self,wall, phi):
        if wall == 'LEFT_WALL':
            self.__aP[1] += self.__aW[1]
            self.__Su[1] += 2 * self.__aW[1] * phi
        elif wall == 'RIGHT_WALL':
            self.__aP[-2] += self.__aE[-2]
            self.__Su[-2] += 2 * self.__aE[-2] * phi       

if __name__ == '__main__':
    
    coef1 = Coefficients(5)
    print(coef1.aP(), coef1.aE(), coef1.aW(), coef1.Su(), sep = '\n')

    ap = coef1.aP()
    ap[2] = 25
    print(ap, coef1.aP(),sep='\n')
    
    ae = coef1.aE()
    aw = coef1.aW()
    su = coef1.Su()
    ae.fill(5)
    aw.fill(5)
    ap.fill(10)
    coef1.bcDirichlet('LEFT_WALL', 2)
    coef1.bcDirichlet('RIGHT_WALL', 1)
    print(coef1.aP(), coef1.aE(), coef1.aW(), coef1.Su(), sep = '\n')

