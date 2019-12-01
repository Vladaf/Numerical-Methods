import numpy as np

A = np.array([[16,120,0,0],[12,7,54,0],[0,74,678,52],[0,0,245,155]])
B = np.array([27,14,87,36])


def solve_lu3(A,B):

	d = np.array([A[i,i] for i in range(len(A))],float)
	eu = np.array([A[i,i+1] for i in range(len(A)-1)],float)
	el = np.array([A[i+1,i] for i in range(len(A)-1)],float)

	a = np.zeros(len(A),float)
	a[1] = -eu[0]/d[0]

	for i in range(2,len(A)):
		a[i] = -eu[i-1]/(d[i-1]+el[i-1]*a[i-1])

	b = np.zeros(len(A),float)
	b[1] = B[0]/d[0]

	for i in range(2,len(A)):
		b[i] = (-el[i-1]*b[i-1] + B[i-1]) / (d[i-1] + el[i-1]*a[i-1])

	x = np.zeros(len(A),float)
	x[-1] = (-el[-1]*b[-1] + B[-1])/(d[-1] + el[-1]*a[-1])

	for i in range(len(A)-2,-1,-1):
		x[i] = a[i+1]*x[i+1] + b[i+1]
	return x
    
x = solve_lu3(A,B)
print(np.dot(A,x))