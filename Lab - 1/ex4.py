# Task: Considering the most efficient form used in the previous level, write a program to multiply
# two square matrices, with 500 rows and 500 columns, containing real values belonging to
# the range [0.500[ randomly generated. The program should display the time used to multiply
# the matrices.
import timeit
import numpy as np
rnd = np.random
# n defines the dimensions of the vectors and the matrix
n = 500
matriz1 = rnd.uniform(0, 500, size=(n, n))
matriz2 = rnd.uniform(0, 500, size=(n, n))
result = np.zeros((n, n))
starttime = timeit.default_timer()
for i in range(len(matriz1)):
    for j in range(len(matriz2[0])):
        temp = 0
        for k in range(len(matriz2)):
            temp += matriz1[i, k] * matriz2[k, j]
        result[i][j] = temp
print(f"Time: {timeit.default_timer() - starttime:.6f}")
