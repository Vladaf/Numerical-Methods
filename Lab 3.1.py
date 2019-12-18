import math
import random

def bisection(f, a, b, eps):
    while abs(a - b) >= eps:
        c = (a + b) * 0.5
        fa = f(a)
        fb = f(b)
        fc = f(c)
        
        if abs(fc) < eps:
            return c
        
        if fa * fc < 0:
            b = c
        elif fb * fc < 0:
            a = c
    
    return (a + b) * 0.5
    
f = lambda x: (1 + x * x) * math.exp(-x) + math.sin(x)
random.seed(199999)
roots = []
for i in range(1000):
    r1 = random.uniform(0, 10)
    r2 = random.uniform(0, 10)
    if r1 > r2:
        r1, r2 = r2, r1
        
    if not(f(r1) * f(r2) < 0):
        continue
    
    sol = bisection(f, r1, r2, 1e-12)
    if sum(1 for x in roots if abs(x - sol) < 1e-9) == 0:
        roots.append(sol)

print(sorted(roots))