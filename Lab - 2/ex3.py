import time
from multiprocessing import Pool


def contar_decrescente(ls, li):
    while ls > li:
        ls -= 1


if __name__ == '__main__':
    COUNT = 50000000
    pool = Pool(2)
    start = time.time()
    pool.apply_async(contar_decrescente, [COUNT // 2, 0])
    pool.apply_async(contar_decrescente, [COUNT, COUNT // 2])
    pool.close()
    pool.join()
    end = time.time()
    print('Time in seconds: ', end - start)

# Task: Explain the purpose of this program
# Answer: The strategy of this algorithm is to create 2 asynchronous processes where
# each one counts from COUNT to half and the other from half to 0 using pool.join() to ensure that
# both processes are finished before continuing the script

# Task: Compare the result obtained in this code with that obtained in the previous examples. present one
# explanation.
# Answer: This algorithm is much faster as each process is a copy of the parent process (it has its
# own environment) and as the process is cpu bound so the GIL will only affect the single thread within each process
