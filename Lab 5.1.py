import numpy as np


def cauchy(f, x0, y0, T, h):
    n = int(T / h) + 1
    x = [0] * n
    y = [0] * n
    x[0] = x0
    y[0] = y0
    for i in range(1, n):
        x[i] = x[i - 1] + h
        y[i] = y[i - 1] + h * f(x[i - 1], y[i - 1])    
    return x, y


def shooting(f, l, mu1, mu2, h):
    
    xx, z1 = cauchy(lambda x, u: np.array([u[1], f(x, u[0], u[1])]), 0, np.array([mu1, 1]), l, h)
    xx, z2 = cauchy(lambda x, u: np.array([u[1], f(x, u[0], u[1])]), 0, np.array([mu1, 2]), l, h)
    
    z1 = list(map(lambda x: x[0], z1))
    z2 = list(map(lambda x: x[0], z2))
    C = (mu2 - z1[-1]) / (z2[-1] - z1[-1])
    sol = [(1 - C) * z1[i] + C * z2[i] for i in range(len(z1))]
    
    return xx, sol
   
xx, yy = shooting(lambda x, u, du: 100 * u * (u - 1), 0.4, 0, 2, 0.001)

for i in range(len(xx)):
    print("u(" + str(xx[i]) + ") = " + str(yy[i]))