import math

# du/dt = du^2/dx^2 + f(x, t), 0 < x < l, 0 < t < T
# -du/dx(0, t) + s1 u(0, t) = m1(t)
# du/dx(l, t) + s2 u(l, t) = m2(t)
# u(x, 0) = I(x)
# шаг h по X и tau по T

def heat_equation(f, l, T, m1, m2, s1, s2, I, h, tau):
    solution = []
    nx = int(l / h) + 1
    nt = int(T / tau) + 1
    solution.append([I(i * h) for i in range(nx)])
    for i in range(1, nt):
        line = [0.0] * nx
        for j in range(1, nx - 1):
            S = tau / (h * h)
            line[j] = S * solution[-1][j + 1] + (1 - 2 * S) * solution[-1][j] + S * solution[-1][j - 1] + tau * f(j * h, i * tau)
        line[0] = (m1(tau * i) * h - line[1]) / (-1 + s1 * h)
        line[-1] = (m2(tau * i) * h + line[-2]) / (1 + s2 * h)
        solution.append(line)
    return solution

def exact_solution(x, t):
    return math.sin(t * (1 + 2 * x - 3 * x * x))

def op_exact(x, t):
    return (1 + 6 * t + (2 - 3 * x) * x) * math.cos(t + t * (2 - 3 * x) * x) + 4 * t * t * (1 - 3 * x) * (1 - 3 * x) * math.sin(t + t * (2 - 3 * x) * x)

def dx_exact_solution(x, t):
    return t * (2 - 6 * x) * math.cos(t + t * (2 - 3 * x) * x)

def calculate_error(mat1, mat2):
    err = 0.0
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            err = max(err, abs(mat1[i][j] - mat2[i][j]))
    return err

def fill_exact_matrix(l, T, h, tau):
    nx = int(l / h) + 1
    nt = int(T / tau) + 1
    
    return [[exact_solution(j * h, i * tau) for j in range(nx)] for i in range(nt)]

#устойчивость при tau / (h*h) < 1/2 
#при h = 0.1,tau = 0.005...

sigma1 = sigma2 = 0
m1 = lambda t: dx_exact_solution(0, t) + sigma1 * exact_solution(0, t)
m2 = lambda t: dx_exact_solution(1, t) + sigma2 * exact_solution(1, t)

print("sigma1 = sigma2 =", sigma1)
#h = 0.1, tau = 0.005
num = heat_equation(op_exact, 1, 0.1, m1, m2, sigma1, sigma2, lambda x: exact_solution(x, 0), 0.1, 0.005)
exa = fill_exact_matrix(1, 0.1, 0.1, 0.005)
print("h = 0.1, tau = 0.005, error:", calculate_error(num, exa))
#h = 0.1, tau = 0.0025
num = heat_equation(op_exact, 1, 0.1, m1, m2, sigma1, sigma2, lambda x: exact_solution(x, 0), 0.1, 0.0025)
exa = fill_exact_matrix(1, 0.1, 0.1, 0.0025)
print("h = 0.1, tau = 0.0025, error:", calculate_error(num, exa))
#h = 0.05, tau = 0.00125
num = heat_equation(op_exact, 1, 0.1, m1, m2, sigma1, sigma2, lambda x: exact_solution(x, 0), 0.05, 0.00125)
exa = fill_exact_matrix(1, 0.1, 0.05, 0.00125)
print("h = 0.05, tau = 0.00125, error:", calculate_error(num, exa))

sigma1 = sigma2 = 10
m1 = lambda t: dx_exact_solution(0, t) + sigma1 * exact_solution(0, t)
m2 = lambda t: dx_exact_solution(1, t) + sigma2 * exact_solution(1, t)

print("sigma1 = sigma2 =", sigma1)
#h = 0.2, tau = 0.005
num = heat_equation(op_exact, 1, 0.1, m1, m2, sigma1, sigma2, lambda x: exact_solution(x, 0), 0.2, 0.005)
exa = fill_exact_matrix(1, 0.1, 0.2, 0.005)
print("h = 0.2, tau = 0.005, error:", calculate_error(num, exa))
#h = 0.2, tau = 0.0025
num = heat_equation(op_exact, 1.0, 0.1, m1, m2, sigma1, sigma2, lambda x: exact_solution(x, 0), 0.2, 0.0025)
exa = fill_exact_matrix(1, 0.1, 0.2, 0.0025)
print("h = 0.2, tau = 0.0025, error:", calculate_error(num, exa))

num = heat_equation(op_exact, 1, 0.1, m1, m2, sigma1, sigma2, lambda x: exact_solution(x, 0), 0.05, 0.00125)
exa = fill_exact_matrix(1, 0.1, 0.05, 0.00125)
print("h = 0.05, tau = 0.00125, error:", calculate_error(num, exa))

sigma1 = sigma2 = 100
m1 = lambda t: dx_exact_solution(0, t) + sigma1 * exact_solution(0, t)
m2 = lambda t: dx_exact_solution(1, t) + sigma2 * exact_solution(1, t)

print("sigma1 = sigma2 =", sigma1)
#h = 0.1, tau = 0.005
num = heat_equation(op_exact, 1, 0.1, m1, m2, sigma1, sigma2, lambda x: exact_solution(x, 0), 0.1, 0.005)
exa = fill_exact_matrix(1, 0.1, 0.1, 0.005)
print("h = 0.1, tau = 0.005, error:", calculate_error(num, exa))
#h = 0.1, tau = 0.0025
num = heat_equation(op_exact, 1, 0.1, m1, m2, sigma1, sigma2, lambda x: exact_solution(x, 0), 0.1, 0.0025)
exa = fill_exact_matrix(1, 0.1, 0.1, 0.0025)
print("h = 0.1, tau = 0.0025, error:", calculate_error(num, exa))
#h = 0.05, tau = 0.00125
num = heat_equation(op_exact, 1, 0.1, m1, m2, sigma1, sigma2, lambda x: exact_solution(x, 0), 0.05, 0.00125)
exa = fill_exact_matrix(1, 0.1, 0.05, 0.00125)
print("h = 0.05, tau = 0.00125, error:", calculate_error(num, exa))