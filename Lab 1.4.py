import numpy as np
import math
from timeit import default_timer as timer

def jacobi(A, B, eps):
    x = [1] * len(B)
    it = 0
    while True:
        xn = [0] * len(B)
        for i in range(len(x)):
            s1 = 0
            s2 = 0
            for j in range(i):
                s1 += A[i][j] * x[j]
            for j in range(i + 1, len(B)):
                s2 += A[i][j] * x[j]
            xn[i] = (B[i] - s1 - s2) / A[i][i]

        if (math.sqrt(sum([(xn[i] - x[i]) * (xn[i] - x[i]) for i in range(len(B))])) < eps):
            return xn
        it += 1
        if (it > 100):
            return xn
        x = xn

def jacobi_vec(A, B, eps):
    x = np.array([1] * len(B))
    U = np.triu(A, k = 1) #верхняя диагональная матрицу
    L = np.tril(A, k = -1) #нижняя диагональная матрицу
    D = np.diag(A)
    D = np.array([1 / d for d in D])
    D = np.diagflat(D) #обратная к диагональной матрице
    
    it = 0
    while True:
        xn = np.dot(D, B - np.dot(L + U, x))
        if (np.linalg.norm(xn - x) < eps):
            return xn
        it += 1
        if (it > 100):
            return xn
        x = xn
        

A = [[0.35, 0.4, 1], [0.7, 0.8, 0.09], [0.15, 0.5, 0.21]]
B = [1, 2, 3]

sol = jacobi(A, B, 1e-6)
print("solution", sol)
print(np.linalg.norm(np.dot(np.matrix(A), np.array(sol)) - B), ("bad!", "ok!")[np.linalg.norm(np.dot(np.matrix(A), np.array(sol)) - B) < 1e-6])

sol = list(jacobi_vec(np.matrix(A), np.array(B), 1e-6))
print("solution", sol)
print(np.linalg.norm(np.dot(np.matrix(A), np.array(sol)) - B), ("bad!", "ok!")[np.linalg.norm(np.dot(np.matrix(A), np.array(sol)) - B) < 1e-6])

start = timer()
for i in range(10000):
    sol = jacobi(A, B, 1e-6)
end = timer()

loops = end - start

start = timer()
AA = np.matrix(A)
bb = np.array(B)
for i in range(10000):
    sol = jacobi_vec(AA, bb, 1e-6)
end = timer()

vectorization = end - start

print("time of loops", loops)
print("time of vectorization", vectorization)