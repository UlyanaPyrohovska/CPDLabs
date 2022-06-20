import shutil
import time
import threading
if __name__ == '__main__':
    # Versao sequencial
    print("Sequential copying of files")
    inicio = time.time()
    for k in range(10):
        fileName1 = "fich" + str(k + 1) + ".dat"
        fileName2 = "outFich" + str(k + 1) + ".dat"
        shutil.copy(fileName1, fileName2)
    print(f"\tTime used for sequential copying of files = {time.time()-inicio}")
    # Versao com threads
    print("Multi-threaded file copying")
    inicio = time.time()
    threads = []
    for k in range(10):
        fileName1 = "fich" + str(k + 1) + ".dat"
        fileName2 = "outFich" + str(k + 1) + ".dat"
        t = threading.Thread(target=shutil.copy, args=[fileName1, fileName2])
        threads.append(t)
        t.start()
    for i in range(10):
        threads[i].join()
    print(f"\tTime used in multi-threading file copying = {time.time() - inicio}")
# Task: Explain what the program does

# Answer: This program copies data from "fich" + str(k + 1) + ".dat" to "outFich" + str(k + 1) + ".dat"
# in a loop firstly by using sequential instructions and by multithreading ( creating 10 threads
# and running them for copying the files)

# Task: Explain the difference in performance observed

# Answer:The difference is signifficant because of the I/O instructions whenever a thread has to wait for an I/O
# instruction, the thread will give a notification and the next thread in the queue will start/continue executing
# thus limiting the time wasted waiting for I/O instructions making the multithreaded program run faster
