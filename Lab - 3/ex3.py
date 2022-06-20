import time
inicio = time.time()
for k in range(10):
    fileName = "fich"+str(k+1)+".dat"
    with open(fileName, 'wb') as file:
        for i in range((k+1)*1000000):
            file.write(i.to_bytes(4, byteorder='big', signed=False))
print(f"Tempo escrita = {time.time()-inicio}")

# Task: Explain what the program does

# Answer: The program saves starting time and creates 10 files in a loop with the names "fich"+str(k+1)+".dat" and writes
# (k+1)*1000000 integers into each file transforming it into bytes in a big byteorder. After writing
# in the files program prints the time spent on executing these instructions.
