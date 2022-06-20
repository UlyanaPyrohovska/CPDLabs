import timeit
import numpy as np

rnd = np.random
n = 10000
vetor = rnd.randint(1000, size=n)
melhorTempo = 9999999  # A big value
for i in range(3):  # Makes 3 time measurements and shows the best
    print(f"Measurement {i + 1} for {n} elements...")
    starttime = timeit.default_timer()
    soma = 0.0
    for j in range(n):
        soma += vetor[j]
    tempo = timeit.default_timer() - starttime
    print(f"\t {tempo} seconds")
    if tempo < melhorTempo:
        melhorTempo = tempo
print(f"Best sum time for {n} elements: {melhorTempo} seconds")
# print(vetor.dtype)
print(f"Bandwidth of da RAM: {n * 4 / melhorTempo / (1024 * 1024):.2f} Mega Bytes per second")

# Task: ▪ Identify the instructions where the time of the sum of the vector elements is calculated
# Answer: 10 and 14 lines
# Task: ▪ Interpret the bandwidth calculation expression (n*4/bestTime/(1024*1024)
# Answer: 4 - number of numbers in the list * 4(bytes) each is in 32int = 4 bytes
# divided by the best time counted and transferred to the mb per second
