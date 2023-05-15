from array import *
import time as t
start_time = t.time()
L = array("i", [1,2])
for i in range(2,48):
    L.append((L[i-1] + L[i-2])//(L[i-1] - L[i-2]))

print(L)

frequencies = {}
for n in L:
    if n not in frequencies:
        frequencies[n] = 1
    else:
        frequencies[n] += 1

print(frequencies)

moda = []
max_val = max(frequencies.values())
for key in frequencies:
    if frequencies[key] == max_val:
        moda.append(key)

print(moda)
print(t.time() - start_time)