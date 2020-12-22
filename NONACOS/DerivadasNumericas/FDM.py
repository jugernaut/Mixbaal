#!/usr/bin/env python
# coding: utf-8

# Cálculo de derivadas numéricas
# Autor: Luis M. de la Cruz Salas
# Rev: mar jul  7 11:12:13 CDT 2020


import numpy as np
import matplotlib.pyplot as plt
    
def forwardFD(u,x,h):
    """
    Esquema de diferencias finitas hacia adelante.
    
    Parameters
    ----------
    u : función. 
    Función a evaluar.
    
    x : array
    Lugar(es) donde se evalúa la función
    
    h : array
    Tamaño(s) de la diferencia entre u(x+h) y u(x).
    
    Returns
    -------
    Cálculo de la derivada numérica hacia adelante.
    """
    return (u(x+h)-u(x))/h

def backwardFD(u,x,h):
    """
    Esquema de diferencias finitas hacia atrás.
    
    Parameters
    ----------
    u : función. 
    Función a evaluar.
    
    x : array
    Lugar(es) donde se evalúa la función
    
    h : array
    Tamaño(s) de la diferencia entre u(x+h) y u(x).
    
    Returns
    -------
    Cálculo de la derivada numérica hacia atrás.
    """
    return (u(x)-u(x-h))/h


def centeredFD(u,x,h):
    """
    Esquema de diferencias finitas centradas.
    
    Parameters
    ----------
    u : función. 
    Función a evaluar.
    
    x : array
    Lugar(es) donde se evalúa la función
    
    h : array
    Tamaño(s) de la diferencia entre u(x+h) y u(x).
    
    Returns
    -------
    Cálculo de la derivada numérica centrada.
    """
    return (u(x+h)-u(x-h))/(2*h)


def D3_FD(u,x,h):
    """
    Esquema de diferencias finitas usando 4 puntos, orden 3.
    
    Parameters
    ----------
    u : función. 
    Función a evaluar.
    
    x : array
    Lugar(es) donde se evalúa la función
    
    h : array
    Tamaño(s) de la diferencia entre u(x+h) y u(x).
    
    Returns
    -------
    Cálculo de la derivada numérica con 4 puntos.
    """
    return (2*u(x+h) + 3*u(x) - 6*u(x-h) + u(x - 2*h))/(6*h)

def line(x,x0,x1,y0,y1):
    """
    Dados dos puntos en el plano, cálcula la pendiente de
    la recta que pasa por esos puntos y regresa los puntos
    que pasan por esa recta.
    """
    return ((y1-y0)/(x1-x0))*(x-x0) + y0



#----------------------- TEST OF THE MODULE ----------------------------------   
if __name__ == '__main__':
    
    # Definimos un arreglo con diferentes tamaños de h:
    N = 5
    h = np.zeros(N)

    h[0] = 1.0
    for i in range(1,N):
        h[i] = h[i-1] * 0.5

    # Definimos un arreglo con valores de 1.0 (donde evaluaremos el cos(x)):
    x = np.ones(N)
    
    aprox = np.array([h,
             np.cos(x), 
             forwardFD(np.sin,x,h), 
             backwardFD(np.sin,x,h), 
             centeredFD(np.sin,x,h),
             FD_D3(np.sin,x,h) ])