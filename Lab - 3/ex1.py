import threading
import time


def conecta():  # simula uma ligação remota a um servidor
    print("\tconnected")
    time.sleep(2)
    print("\tdisconnected")


if __name__ == '__main__':
    numero_de_ligacoes = 20
    inicio = time.time()
    print("Start of sequential processing")
    for i in range(numero_de_ligacoes):
        print(f'{i + 1}ª connection')
        conecta()
    fim = time.time()
    print(f'Time spent to perform {numero_de_ligacoes}ª sequential connections: {fim - inicio}s')
    print("Start of multi-threading processing")
    # multi-threaded
    threads = []
    inicio = time.time()
    for i in range(numero_de_ligacoes):
        t = threading.Thread(target=conecta)
        threads.append(t)
        t.start()
    for i in range(numero_de_ligacoes):
        threads[i].join()
    fim = time.time()
    print(f'Time spent to perform {numero_de_ligacoes} multi-threading connections: {fim - inicio}s')
# Task: Explain the difference in performance between sequential processing and multi-threading.
# Relate to the sleep instruction.

# Answer: For the sequential processing for another connection to start it had to wait 2s and disconnect
# but for the multiprocessing it starts another thread without waiting
# for the previous to end (simulating the I/O instructions)

# Task: Change the number of connections to 20 and analyze and explain the results obtained

# Answer: By changing the number of connections to 20 we can see the significant difference in time spent for connecting
# The time spent using multithreading is 20 times faster than the sequential. For multithreading it's 2 seconds which took
# the time for creating the threads one by one while waiting for 2 seconds only once.

