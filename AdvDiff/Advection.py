#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:46:43 2018

@author: luiggi
"""

import numpy as np
from Coefficients import Coefficients

class Advection1D(Coefficients):
    
    def __init__(self, nvx = None, rho = None, dx = None):
        super().__init__(nvx)
        self.__nvx = nvx
        self.__rho = rho
        self.__dx = dx
        self.__u = np.zeros(nvx-1)

    def __del__(self):
        del(self.__nvx)
        del(self.__rho)
        del(self.__dx)
        del(self.__u)

    def setVel(self, u):
    	self.__u = u

    def u(self):
    	return self.__u
    
    def calcCoef(self):
        aE = self.aE()
        aW = self.aW()
        aP = self.aP()

        for i in range(self.__nvx):
            aE[i] += np.max(self.__u[i],0)
            aW[i] += np.max(-self.__u[i-1],0)
            aP[i] += aE[i] + aW[i] + self.__rho * (self.__u[i] - self.__u[i-1])

if __name__ == '__main__':
    
    nvx = 6
    u = np.sin(np.linspace(0,1,nvx))
    print(u)
    af1 = Advection1D(5, 5, 1)
    af1.setVel(u)
    print(af1.u())
    af1.calcCoef()
    print(af1.aP(), af1.aE(), af1.aW(), af1.Su(), sep = '\n')

    af1.bcDirichlet('LEFT_WALL', 2)
    af1.bcDirichlet('RIGHT_WALL', 1)
    print(af1.aP(), af1.aE(), af1.aW(), af1.Su(), sep = '\n')



