# Change the level 4 program by implementing the most efficient way to get the terms of the
# Fibonacci sequence observed at level 3.

import time
from multiprocessing import Process, Queue, current_process, Manager


def fibonacci(n):
    a, b = 0, 1
    for item in range(n):
        a, b = b, a + b
    return a


def mostrar_dicionario(dicionario):
    for n in dicionario.keys():
        print(f"Fib({n}) = {dicionario[n]}")


def gerar_chaves(fibo_dict, qtd):
    for i in range(qtd):
        fibo_dict[i + 1] = None


def calcular_valores(q, fibo_dict):
    cont = 0
    while not q.empty():
        n = q.get()
        if n <= 2:
            fibo_dict[n] = 1
        else:
            if fibo_dict[n - 1] and fibo_dict[n - 2]:
                fibo_dict[n] = fibo_dict[n - 1] + fibo_dict[n - 2]
            else:
                fibo_dict[n] = fibonacci(n)
        cont = cont + 1
    print(f"{current_process().name} - calculou {cont} termo(s) da série")


def calcular_valores_pool(fibo_dict, n):
    # print(f"Processo {current_process().name} a calcular Fib({n})")
    fibo_dict[n] = fibonacci(n)


if __name__ == '__main__':
    qtd_valores = 1000
    numero_de_processos = 4
    inicio = time.time()
    # Creating a manager which controls a server process which holds Python objects and allows other processes to
    # manipulate them using proxies, in this case a dictionary
    manager = Manager()
    # Alowing to assign dictionary which is in the manager
    dicionario_fibonacci_par = manager.dict()
    # Generating keys for the dictionary and assign the value of the keys to the dictionary
    gerar_chaves(dicionario_fibonacci_par, qtd_valores)
    fila_de_valores_fibonacci = Queue()
    # print(dicionario_fibonacci_par.keys())
    for k in dicionario_fibonacci_par.keys():
        fila_de_valores_fibonacci.put(k)
    lista_de_processos = []
    for _ in range(numero_de_processos):
        p = Process(target=calcular_valores, args=(fila_de_valores_fibonacci, dicionario_fibonacci_par))
        p.start()
        lista_de_processos.append(p)
    # Joining to every process in the process list, untill all processes are finished
    [p.join() for p in lista_de_processos]
    fim = time.time()
    print(
        f"Tempo utilizado para calcular os primeiros {qtd_valores} termos da série de Fibonacciutilizando "f" multiprocessamento {fim - inicio:.10f}s")
    # mostrar_dicionario(dicionario_fibonacci_par)