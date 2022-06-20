import timeit
import numpy as np

# Task: Develop code that does the same as in number 4 (matrix multiplication),
# but using the matmul function from the NumPy library.

rnd = np.random

# n defines the dimensions of the vectors and the matrix
n = 500
matriz1 = rnd.uniform(0, 500, size=(n, n))
matriz2 = rnd.uniform(0, 500, size=(n, n))
starttime = timeit.default_timer()
np.matmul(matriz1, matriz2)
print(f"Time: {timeit.default_timer() - starttime:.6f}")
