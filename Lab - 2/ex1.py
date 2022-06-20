import time

COUNT = 50000000


def contar_decrescente(ls, li):
    while ls > li:
        ls -= 1


inicio = time.time()
contar_decrescente(COUNT, 0)
fim = time.time()
print(f'Time in seconds: {fim - inicio}')

# Task: Explain the purpose of this program;
# Answer: The program shows the time it takes to iterate COUNT times by decrementing variable ls

# Task: Characterize the program in terms of CPU-bound or I/O Bound.
# Answer: This program is CPU-bound because it is an execution of instructions using just CPU and it
# isn't waiting for input/output instructions
