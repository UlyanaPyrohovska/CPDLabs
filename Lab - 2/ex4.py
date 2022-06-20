import multiprocessing
import random
from timeit import default_timer as timer


def criar_e_ordenar(n):
    rand = random.Random(50)
    x = [rand.randint(0, 100) for _ in range(n)]
    x.sort()
    return x


if __name__ == "__main__":
    numero_CPUs = multiprocessing.cpu_count()
    print(f'Number of CPUs: {numero_CPUs}')
    vetores_a_gerar = [2, 4, 6, 15]
    dimensoes_dos_vetores = [10 ** 2, 10 ** 3, 10 ** 4, 10 ** 6]
    for numero_de_elementos in dimensoes_dos_vetores:
        print(f'Number of elements in vector: {numero_de_elementos}')
    for qtd_vetores_a_gerar in vetores_a_gerar:
        print(f'\tNumber of vectors to generate and sort:{qtd_vetores_a_gerar}')
    dimensoes = []
    for i in range(qtd_vetores_a_gerar):
        dimensoes.append(numero_de_elementos)
    # dimensoes1 = [d for i in range(qtd_vetores_a_gerar)]
    # print(dimensoes ,dimensoes1)
    # Aplicar a função sequencialmente
    resultado = []
    inicio = timer()
    for d in dimensoes:
        resultado.append(criar_e_ordenar(d))
    # resultado = [createandsort(d) for d in dimensoes]
    fim = timer()
    print("\t\tTime for sequential sorting: ", fim - inicio)
    # print(resultado)
    # print([createandsort(d) for d in dimensoes])
    # Utilizando multiprocessamento
    pool = multiprocessing.Pool(processes=numero_CPUs)  # Usa o número de cores físicos da sua máquina
    inicio = timer()
    resultado = pool.map(criar_e_ordenar, dimensoes)
    fim = timer()
    print("\t\tTime for parallel sorting: ", fim - inicio)

# Task: say what each of the following statements does:
#  - pool = multiprocessing.Pool(processes=number_CPUs)
# Answer: In this line we are creating a pool with the maximum processes number equivalent the num of cores my CPU has
#  - the pool.map(createandsort, dimensions)
# Answer: In this line we are passing a list of multiple arguments,
# in this case the dimensions and create_and_sort func dividing the data into "chunk sizes"

# Task: Observe the program output and perform a critical analysis of the observed results. The analysis should take
# into account the dimensions of the vectors, the number of vectors generated and the times observed for sequential
# sorting and sorting using multiprocessing.

# Answer: The greater the number of elements in the vector and of vectors, the longer the execution time. So if we
# use parallelism with larger datasets we can drastically reduce the execution time due to the use of processes with
# smaller individual "datasets" based on the input dataset
