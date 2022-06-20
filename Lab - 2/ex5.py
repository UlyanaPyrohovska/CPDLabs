import multiprocessing as mp
from timeit import default_timer as timer
import numpy as np


def quadrado(nums):
    pnome = mp.current_process().name
    for num in nums:
        resultado = num * num
        print(f"Process {pnome}; the square of the number {num} is {resultado}.")


if __name__ == '__main__':
    numero_CPUs = mp.cpu_count()
    processos = []
    limite_superior = 200
    lista = np.array_split(range(limite_superior), numero_CPUs)
    # creating an array lista which consists of number of arrays equivalent to the number of CPUs
    # by splitting the range of numbers limite_superior
    print('Start of multiprocessing')
    inicio = timer()
    for i in range(numero_CPUs):
        processo = mp.Process(target=quadrado, args=(lista[i],))
        # creating the process to calculate the target function quadrado() with the argument lista[i]
        processos.append(processo)
        processo.start()
        # starting of each process
    for processo in processos:
        processo.join()
        # The join method blocks the execution of the main process until the process whose join method is called
        # terminates. Without the join method, the main process won't wait until the process gets terminated.
    fim = timer()
    print(f"Full multiprocessing in {fim - inicio} seconds")
    print('Start of pooled multiprocessing')
    pool = mp.Pool(processes=numero_CPUs)
    inicio = timer()
    resultado = pool.map(quadrado, lista)
    fim = timer()
    print(f"Full multiprocessing in {fim - inicio} seconds")

# Task: say what each of the following statements does:
# o lista = np.array_split(range(limite_superior), numero_CPUs)
# o processo = mp.Process(target=quadrado, args=(lista[i],))
# o processos.append(processo)
# o processo.start()
# o processo.join()

# Task: Observe the output of the program and check how many processes were created in the processing:
# o No pool - 8 processes created
# o With pool - 3 processes created

# Task: Carry out a critique of the observed results when you significantly change the number of values to be
# calculated. The analysis should take into account the amount of values, the number of processes created and the
# impact on performance.

# Answer: When we significantly increase the limit, the pool is much faster
# The pool only creates the necessary number of processes and only stores in memory
# the processes that are being executed so it's better than creating 8 processes
# and storing them all in memory using space, if the algorithm is CPU bound it is better but if it is I/O bound
# the other choice is better
