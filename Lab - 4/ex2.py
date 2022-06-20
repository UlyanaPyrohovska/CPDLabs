# Write a program that creates two producer processes (pipe_producer and queue_producer) and
# two consumer processes (consumer_pipe and consumer_queue). The process
# producer_pipe must send the names of the students in the group to the consumer_pipe process
# using pipe communication. The producer_queue process must send the names of the
# group students to the consumer_queue process using queue communication. Your
# consumer processes must present the information received.
# The program output should have the following format:

from multiprocessing import Process, Queue, Pipe
import os


def queue_produce(q):
    name = ['Uliana', 'Pyrohovska']
    print(f"\t{name} enviado pelo subprocesso produtor_queue {os.getpid()}")
    q.put(name)


def queue_recieve(q):
    name = q.get()
    print(f"\t{name} recebido pelo subprocesso consumer_queue {os.getpid()}")


def pipe_recieve(p):
    name = p.recv()
    print(f"\t{name} recebido pelo subprocesso consumer_pipe {os.getpid()}")


def pipe_produce(conn):
    name = ['Uliana', 'Pyrohovska']
    print(f"\t{name} enviado pelo subprocesso produtor_pipe {os.getpid()}")
    conn.send(name)
    conn.close()


if __name__ == '__main__':
    q = Queue()
    queue_producer = Process(target=queue_produce, args=(q,))
    queue_producer.start()
    consumer_queue = Process(target=queue_recieve, args=(q,))
    consumer_queue.start()
    queue_producer.join()
    consumer_queue.join()

    conn_pai, conn_filho = Pipe()
    pipe_producer = Process(target=pipe_produce, args=(conn_pai,))
    pipe_producer.start()
    consumer_pipe = Process(target=pipe_recieve, args=(conn_filho,))
    consumer_pipe.start()
    pipe_producer.join()
    consumer_pipe.join()