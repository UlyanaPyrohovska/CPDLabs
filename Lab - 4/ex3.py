import time


def fibonacci(n):
    a, b = 0, 1
    for item in range(n):
        a, b = b, a + b
    return a


def preencher_dicionario_fibonacci_v1(dicionario, qtd):
    for i in range(qtd):
        dicionario[i + 1] = fibonacci(i + 1)


def preencher_dicionario_fibonacci_v2(dicionario, qtd):
    for i in range(qtd):
        if i <= 2:
            dicionario[i] = 1
        else:
            dicionario[i] = dicionario[i - 1] + dicionario[i - 2]


def mostrar_dicionario(dicionario):
    for n in dicionario.keys():
        print(f'Fib({n}) = {dicionario[n]}')


if __name__ == '__main__':
    qtd_valores = 1000
    inicio = time.time()
    dicionario_fibonacci = {}
    preencher_dicionario_fibonacci_v1(dicionario_fibonacci, qtd_valores)
    tempo = time.time() - inicio
    print(f'{tempo:.10f}s to calculate the first {qtd_valores} terms of the Fibonacci series sequentially')
    # print(dicionario_fibonacci)
    mostrar_dicionario(dicionario_fibonacci)
    inicio = time.time()
    dicionario_fibonacci = {}
    preencher_dicionario_fibonacci_v2(dicionario_fibonacci, qtd_valores)
    tempo = time.time() - inicio
    print(f'{tempo:.10f}s to calculate the first {qtd_valores} terms of the Fibonacci series sequentially')
    mostrar_dicionario(dicionario_fibonacci)

# Task: Explain what the program does.

# Answer: The program calculates and stores fibonacci numbers into the dicionary

# Task: What is a dictionary in Python?

# Answer: Dictionary in Python is an unordered collection of data values,
# used to store data values like a map (key-value)

# Task: Comment out the instructions show_dictionary(dictionary_fibonacci),
# change to 10000 the value of qty_values and run the program.
# Explain the difference of observed performance.

# Answer: The v2 is much faster than v1 because you don't have to run the fibonacci function every iteration, and we are
# directly adding the last 2 dictionary values instead of running the function
