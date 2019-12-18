from autograd import jacobian
import autograd.numpy as np


def system(x):
    arr = list()
    arr.append((3+2*x[0])*x[0] - 2*x[1] - 3)
    for i in range(1, len(x)-1):
        arr.append((3+2*x[i])*x[i]-x[i-1]-2*x[i+1]-2)
    arr.append((3+2*x[-1])*x[-1]-x[-2]-4)
    return np.array(arr)


def newton(f, x_init, tol, it_max):
    x_last = x_init
    for k in range(it_max):
        J = jacobian(system)(x_last)
        F = np.array(f(x_last))
        diff = np.linalg.solve(J, -F)
        x_last = x_last + diff

        if np.linalg.norm(diff) < tol:
            break

    return x_last


def cost(x):
    return x[0]**2 / x[1] - np.log(x[1])

n = 10
it_max = 50
tol = 1e-8
x = np.array([2, 3, 5, 9, 7, 3, 5, 1, 2, 4], dtype=float)
sol = newton(system, x, tol, it_max)
print(sol)

