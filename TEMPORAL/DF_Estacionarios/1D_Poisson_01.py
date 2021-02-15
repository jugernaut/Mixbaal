#!/usr/bin/env pyhton
"""
    Construye y resuelve el sistema Ax = b, producto de aplicar \n
    el método de diferencias finitas a la ecuación de Poisson   \n
    en una dimensión, con condiciones de frontera tipo Dirichlet.

Ejecución:

    Solicita del usuario las dimensiones del dominio, \n
    el numero de nodos y el valor de las condiciones.
"""
import numpy as np
import matplotlib.pyplot as plt

#def solExacta(x):
#    return 800 * x + 100
 
def solExacta(x,Ta,Tb,k,L,q):
	return ((Tb-Ta)/L+(q/(2*k))*(L-x))*x+Ta 

def Laplaciano1D(N, diagonal):
    """
        Devuelve la matriz A, del sistema Ax = b. 
        Params:
            N: int
                Número de incognitas. \n
            diagonal: escalar
                Valor de la diagonal principal. \n
        Return:
            A: ndarray
                Matriz NxN, con tres bandas distintas a cero.
    """
    A = np.zeros((N,N))
    A[0,0] = diagonal; A[0,1] = 1
    for i in range(1,N-1):
        A[i,i] = diagonal
        A[i,i+1] = 1
        A[i,i-1] = 1
    A[N-1,N-2] = 1; A[N-1,N-1] = diagonal
    return A

# Comienza la ejecución del programa
print()
print("+----------------------------------------------------+")
print("|      Solucion de la ecuacion de Laplace en 1D      |")
print("+----------------------------------------------------+")
print("| Autor: Luis M. de la Cruz S.                       |")
print("+----------------------------------------------------+")
print("|                 Datos de entrada                   |")
print("+----------------------------------------------------+")

# Tamanio del dominio (se lee del teclado, se toma como cadena, luego se transforma a flotante)
a = 0.0 #float(input('| Punto inicial del dominio      : a = '))
b = 0.02 #float(input('| Punto final del dominio        : b = '))

# Condiciones Dirichlet
boundA = 100.0 #float(input('| Cond. de front. Dirichlet en a : A = '))
boundB = 200.0 #float(input('| Cond. de front. Dirichlet en b : B = '))
print("+----------------------------------------------------+")

q = 1000000.0
Nlist = [4, 8]# 16, 32, 64, 128, 256, 512, 1024, 2048]
error = []
hlist = []
for N in Nlist:
    h = (b-a)/(N+1)
    hlist.append(h)
    x = np.linspace(a,b,N+2)

    ue = solExacta(x,boundA,boundB,0.5,0.02,q)

# Definicion del sistema lineal de N x N
    f = -np.ones(N) * q * h**2       # Lado derecho
    A = 0.5 * Laplaciano1D(N, -2) # Matriz del sistema

    # Aplicacion de las cond. Dirichlet para el calculo correcto de la sol.
    f[0] -= boundA * 0.5
    f[N-1] -= boundB * 0.5

    # La solucion sera guardada en el arreglo u, que es de tamanio N+2, pues incluye las fronteras
    u = np.zeros(N+2)

    # Se utiliza un algoritmo del paquete linalg para obtener la solucion del sistema de N x N
    u[1:N+1] = np.linalg.solve(A,f)

    # Los valores en los extremos son conocidos debido a las cond. Dirichlet
    u[0] = boundA
    u[N+1] = boundB 

    error.append( np.linalg.norm(ue - u, 1) / N)

print(error)
    
#plt.plot(Nlist, error , '--bo')
#plt.plot(hlist, error , '--bo')
#plt.yscale('log')

plt.plot(x, u, '-r.', alpha = 0.5)
plt.plot(x, ue, '-b.', alpha = 0.5)
plt.show()


