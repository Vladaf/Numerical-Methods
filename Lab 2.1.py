import numpy as np

def generate_matrix(n):
    aij = lambda i, j: 1 / (i + j - 1)
    arr = [[aij(i + 1, j + 1) for i in range(n)] for j in range(n)]
    return np.array(arr)

def power_method(A):
    q = [1] * A.shape[0]
    q /= np.linalg.norm(q)
    while True:
        z = np.dot(A, q)
        z /= np.linalg.norm(z)
        if np.linalg.norm(q - z) < 1e-6:
            break
        q = z
    return np.dot(np.dot(A, q), q), q

for n in range(2, 11):
    print("n =", n)
    H = generate_matrix(n)
    print(H)
    l, v = power_method(H)
    print("max(abs(eigenvalue)) =", l, "\neigenvector =", v)