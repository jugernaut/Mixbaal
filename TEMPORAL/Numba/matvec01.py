from numba import jit
import numpy as np
import time

n = 5

A = np.ones((n,n))
x = np.ones(n)

#print("A =", A)
#print("x =", x)
#print("b=", b)

@jit(nopython=True)
def matriz_vector(A,x):
	b = np.zeros(n)
	for i in range(n):
		for j in range(n):
			b[i] += A[i][j] * x[j]
	return b

start = time.time()
matriz_vector(A,x)
end = time.time()
print("Elapsed (with compilation) = %s" % (end - start))

start = time.time()
matriz_vector(A,x)
end = time.time()
print("Elapsed (after compilation) = %s" % (end - start))

start = time.time()
matriz_vector(A,x)
end = time.time()
print("Elapsed (Tercera) = %s" % (end - start))



#print("b =", b)

