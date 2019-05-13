import numpy as np
import numba

@numba.jit(nopython=True, parallel=True)

def logistic_regression(Y, X, w, iterations):
    for i in range(iterations):
        w -= np.dot(((1.0 / (1.0 + np.exp(-Y * np.dot(X, w))) - 1.0) * Y), X)
    return w

N = 5
D = 2
Y = np.ones(N)
X = np.ones((N,D))
w = np.ones(D)

iterations = 2

print(Y)
print(X)
print(w)

wr = logistic_regression(Y,X,w,iterations)

print(wr)

