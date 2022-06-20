from multiprocessing import Process, Queue, Pipe
import os
import random


def funcao_comunicacao_queue(q):
    print(f"\tI am in the function funcao_comunicacao_queue and I am the process {os.getpid()}")
    valor = random.randint(1, 10)
    q.put(valor)
    # putting the random value from 1 to 10 in the queue


def funcao_comunicacao_pipe(conn):
    print(f"\tI'm in the funcao_comunicacao_pipe function and I'm the process {os.getpid()}")
    # Sending an array of items from one socket to another
    conn.send(['Olá', 'mundo', 'abril', 2022])
    # closes the connection
    conn.close()


if __name__ == '__main__':
    print(f"main process {os.getpid()}")
    # Declaring the queue
    q = Queue()
    processo_1 = Process(target=funcao_comunicacao_queue, args=(q,))
    processo_1.start()
    valor = q.get()
    # poping the last item from the queue
    print(f"amount received: {valor}")
    processo_1.join()
    # creating a connection between 2 processes, in this case parent and child, the standard output of one
    # process becomes the standard input of the other (link between 2 processes)
    conn_pai, conn_filho = Pipe()
    processo_2 = Process(target=funcao_comunicacao_pipe, args=(conn_filho,))
    processo_2.start()
    # returns an object with empty bytes to signal that the client closed the connection
    valor = conn_pai.recv()
    print(f"amount received: {valor}")
    processo_2.join()

# Task: Say what each of the following statements does:
# q = Queue()
# q.put(value)
# value = q.get()
# parent_conn, child_conn = Pipe()
# conn.send(['Hello', 'world', 'April', 2022])
# conn.recv()
# conn.close()
