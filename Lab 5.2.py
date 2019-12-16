import math

def solve_eq(f, l, m1, m2, h):
    N = int(l / h + 0.5)
    u = [0] * (N + 1)
    u[0] = m1
    u[N] = m2
    it = 0
    while True:
        xi = dict()
        th = dict()
        xi[1] = 0
        th[1] = m1
        for i in range(1, N):
            xi[i + 1] = 1 / (2 - xi[i])
            th[i + 1] = (-h * h * f(i * h, u[i]) + th[i]) / (2 - xi[i])
        U = [0] * (N + 1)
        U[N] = m2
        for i in reversed(range(0, N)):
            U[i] = xi[i + 1] * U[i + 1] + th[i + 1]
        if sum((U[i] - u[i]) * (U[i] - u[i]) for i in range(N + 1)) < 1e-9: 
            return U
        if it > 100: 
            return U
        it += 1
        u = U.copy()

sol = solve_eq(lambda xx, uu: -math.exp(uu), 1, 0, 0, 0.1)

print(sol)

for i in range(11):
    print("u(" + str(0.1 * i) + ") =", sol[i])