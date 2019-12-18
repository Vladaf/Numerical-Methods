import numpy as np

def sor(A, b, omega, initial, tol):

    phi = initial[:]
    residual = np.linalg.norm(np.matmul(A, phi) - b)
    while residual > tol:
        for i in range(A.shape[0]):
            sigma = 0
            for j in range(A.shape[1]):
                if j != i:
                    sigma += A[i][j] * phi[j]
            phi[i] = (1 - omega) * phi[i] + (omega / A[i][i]) * (b[i] - sigma)
        residual = np.linalg.norm(np.matmul(A, phi) - b)
    return phi

def cg(A, b, tol, it_max):
    it = 0
    x = 0
    r = np.copy(b)
    r_prev = np.copy(b)
    rho = np.dot(r, r)
    p = np.copy(r)
    while (np.sqrt(rho) > tol*np.sqrt(np.dot(b, b)) and it < it_max):
        it += 1
        if it == 1:
            p[:] = r[:]
        else:
            beta = np.dot(r, r)/np.dot(r_prev, r_prev)
            p = r + beta*p
            w = np.dot(A, p)
            alpha = np.dot(r, r)/np.dot(p, w)
            x = x + alpha*p
            r_prev[:] = r[:]
            r = r - alpha*w
            rho = np.dot(r, r)
    if it==it_max:
        return x, it
    else:
        return x, it

    alfa=0.3
    N = 3

    A=np.zeros((N,N),float)
    b=np.zeros(N, float)

    A[0,0]=2
    A[0,1]=-1+alfa
    A[N-1,N-1]=2
    A[N-1,N-2]=-1+alfa
    b[0]=1-alfa
    b[N-1]=1+alfa

    for i in range(1,N-1,1):
        A[i,i]=2
        A[i,i+1]=-1+alfa
        A[i,i-1]=-1+alfa
        b[i]=0

    tol = 1e-8
    omega = 0.3

    x0 = np.zeros(3)

    xsor = sor(A, b, omega, x0, tol)
    print(xsor)

    xcg = cg(A, b, tol, 100)
    print(xcg)