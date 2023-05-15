import time as t
Iterable = []
for i in range(0,1000):
    Iterable.append(i)

#for in iterable
start_time = t.time()
for i in Iterable:
    a = i+10
print("Iterable for loop: ", t.time() - start_time)

#c-like for 
start_time = t.time()
i = 0
while i < 1000:
    a = i+10
    i+=1
print("C-like for loop:   ", t.time() - start_time)