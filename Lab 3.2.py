import math
import random

def f(x):
    return 4.0 * math.sin(x) + 1.0 - x

def secant_method(g, x0, x1, eps):
    iters = 0 
    while True:
        f0 = g(x0)
        f1 = g(x1)
        xn = x1 - (x1 - x0) * f1 / (f1 - f0)
        if (abs(x1 - xn) < eps):
            return xn
        x0 = x1
        x1 = xn
        iters += 1
        if (iters > 100):
            return float('NaN')

random.seed(1223) 

roots = []
for i in range(50):
    r1 = random.uniform(-10, 10)
    r2 = random.uniform(-10, 10)
    sol = secant_method(f, r1, r2, 1e-9)
    if not(any(abs(x - sol) < 1e-9 for x in roots)):
        roots.append(sol)
    
roots.sort()

print(roots)