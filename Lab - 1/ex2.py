# Change the program to automatically take measurements for vector sizes equal to one
# thousand, ten thousand, one hundred thousand, one million, ten million and twenty million
# (for example, you can put these values in a list and use a for iterating over that list ). It is
# also necessary for your program to add the different bandwidth measurements to a list and
# then display their average. For example, if you use a bwRAM list to store measurements,
# the average will be: sum(bwRAM)/len(bwRAM)
import timeit
import numpy as np

rnd = np.random
n = 10000
sizes = [1000, 10000, 100000, 1000000, 10000000, 20000000]
vals = []
for l in sizes:
    vector = rnd.randint(1000, size=l)
    melhorTempo = 9999999
    for i in range(3):  # Makes 3 time measurements and shows the best
        print(f"Measurement {i + 1} for {l} elements...")
        starttime = timeit.default_timer()
        soma = 0.0
        for j in range(l):
            soma += vector[j]
        tempo = timeit.default_timer() - starttime
        print(f"\t {tempo} seconds")
        if tempo < melhorTempo:
            melhorTempo = tempo
    print(f"Best sum time for {l} elements: {melhorTempo} seconds")
    bandw = l * 4 / melhorTempo / (1024 * 1024)
    vals.append(bandw)
    print(f"Bandwidth of the RAM: {bandw:.2f} Mega Bytes per second")
print(f"Average RAM Bandwidth: {sum(vals) / len(vals):.2f}")
