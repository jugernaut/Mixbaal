#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:46:43 2018

@author: luiggi
"""

from Coefficients import Coefficients

class Advection1D(Coefficients):
    
    def __init__(self, nvx = None, Gamma = None, dx = None):
        super().__init__(nvx)
        self.__nvx = nvx
        self.__Gamma = Gamma
        self.__dx = dx

    def __del__(self):
        del(self.__nvx)
        del(self.__Gamma)
        del(self.__dx)
    
    def calcCoef(self):
        aE = self.aE()
        aW = self.aW()
        aP = self.aP()
        
        aE += self.__Gamma / self.__dx
        aW += self.__Gamma / self.__dx
        aP += aE + aW

#        for i in range(self.__nvx):
#            aE[i] += self.__Gamma / self.__dx
#            aW[i] += self.__Gamma / self.__dx
#            aP[i] += aE[i] + aW[i]

if __name__ == '__main__':
    
    af1 = Advection1D(5, 5, 1)
    af1.calcCoef()
    print(af1.aP(), af1.aE(), af1.aW(), af1.Su(), sep = '\n')

    ap = af1.aP()
    ae = af1.aE()
    aw = af1.aW()
    su = af1.Su()

    af1.bcDirichlet('LEFT_WALL', 2)
    af1.bcDirichlet('RIGHT_WALL', 1)
    print(af1.aP(), af1.aE(), af1.aW(), af1.Su(), sep = '\n')