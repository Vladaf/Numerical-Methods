import numpy as np
import math
import matplotlib.pyplot as plt

def runge_kutta(f, x0, y0, T, h):
    xx = [x0]
    yy = [y0]
    while(True):
        xn = xx[-1]
        yn = yy[-1]
        if (xn + h > T): 
            break
        q1 = f(xn, yn)
        q2 = f(xn + 0.5 * h, yn + 0.5 * h * q1)
        q3 = f(xn + 0.5 * h, yn + 0.5 * h * q2)
        q4 = f(xn + h, yn + h * q3)
        yn1 = yn + h / 6 * (q1 + 2 * q2 + 2 * q3 + q4)
        xx.append(xn + h)
        yy.append(yn1)
    
    return xx, yy

xx, uu = runge_kutta(lambda x, uv: np.array([uv[1], -math.sin(uv[0])]), 0, np.array([1, 0]), 4 * math.pi, 0.01)
uu = [x[0] for x in uu]

plt.plot(xx, uu)
plt.savefig('diagram.png')