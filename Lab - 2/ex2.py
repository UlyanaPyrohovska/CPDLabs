# threads Múltiplos
import time
from threading import Thread

COUNT = 50000000


def contar_decrescente(ls, li):
    while ls > li:
        ls -= 1


inicio = time.time()
thread_1 = Thread(target=contar_decrescente, args=(COUNT, COUNT // 2,))
thread_2 = Thread(target=contar_decrescente, args=(COUNT // 2, 0,))
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
fim = time.time()
print(f'Time in seconds: {fim - inicio}')

# Task: Explain the purpose of this program;
# Answer: The program does the same thing the previous does but this time we are creating 2 threads and
# splitting the task between them by passing medium point

# Task: Compare the result obtained in this code with that obtained in the level 1 code.explanation.

# Answer: # The algorithm takes longer than the previous one because the threads are executed in order and each
# thread can be interrupted by the GIL when the thread is forced to release it after a certain defined time and if
# "nobody" acquires the GIL the thread can continue execution
