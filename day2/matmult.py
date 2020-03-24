# Program to multiply two matrices using nested loops
import random
import numpy as np


@profile
def generate_matrix(n_rows, n_columns):
    m = []
    for i in range(n_rows):
        m.append([random.randint(0,100) for r in range(n_columns)])
    return m

@profile
def generate_matrix_np(n_rows, n_columns):
    return np.random.randint(100, size=(n_rows, n_columns))

@profile
def generate_matrix_empty(n_rows, n_columns):
    m = []
    for i in range(n_rows):
        m.append([0] * (n_columns))
    return m

@profile
def matmult(X, Y):
    result = generate_matrix_empty(len(X), len(Y[0]))
    # iterate through rows of X 
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result

@profile
def matmult_np(X, Y):
    return np.dot(X, Y)

N = 250

### Naive version
X = generate_matrix(N, N)
Y = generate_matrix(N, N+1)
result = matmult(X, Y)

### Numpy version (OPTIMIZED!)
X = generate_matrix_np(N, N)
Y = generate_matrix_np(N, N+1)
result = matmult_np(X, Y)

for r in result:
    print(r)
