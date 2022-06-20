import timeit
import numpy as np


rnd = np.random
# n defines the dimensions of the vectors and the matrix
n = 5000
vetor = rnd.uniform(0, 1000, size=n)
matriz = rnd.uniform(0, 1000, size=(n, n))
resultado = np.zeros(n)


# first implementation
def firstimpl():
    starttime = timeit.default_timer()
    for i in range(len(matriz)):  # number of matrix rows
        for j in range(len(vetor)):  # number of elements in vector
            resultado[i] += matriz[i, j] * vetor[i]
    print(f"Time 1: {timeit.default_timer() - starttime:.6f}")
    print(f"First elements of result vector: {resultado[0:5]}")


# second implementation
def secondimpl():
    starttime = timeit.default_timer()
    for i in range(len(matriz)):  # number of matrix rows
        temp = 0
        for j in range(len(vetor)):  # number of elements in vector
            temp += matriz[i, j] * vetor[i]
    resultado[i] = temp
    print(f"Time 2: {timeit.default_timer() - starttime:.6f}")
    print(f"Primeiros elementos do vetor resultado: {resultado[0:5]}")


if __name__ == '__main__':
    print(f"First Implemenation\n")
    firstimpl()
    print(f"\nSecond Implemenation\n")
    secondimpl()

# Task: Analyze the results observed when you run the program and explain the difference in performance
# Answer: Second implementation takes less time due to temporary variable
# Task: Try running the program varying the n between 500 and 5000.
# Relate the value of n with the variation of the performance of the two methods
# Answer: The second implementation is much faster than the first one,
# the bigger the n the bigger the performance difference
