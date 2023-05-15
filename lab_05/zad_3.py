from zad_1 import move
from zad_2 import possible_move
import time as t

def hanoi_iter(src, dest, buff):
    i = 1
    while len(src) != 0 or len(buff) != 0:
        if i % 3 == 1:
            possible_move(src, dest)
        elif i % 3 == 2:
            possible_move(src, buff)
        else:
            possible_move(buff, dest)
        print(f"""Iteracyjnie (i = {i}:
    Source: {src}
    Buffer: {buff}
    Destination: {dest}""")
        i += 1
    return i


global steps_rek
steps_rek = 0

def hanoi_rek(n, src, dest, buff):
    global steps_rek
    steps_rek += 1
    if len(src) == 0 and len(buff) == 0:
        return
    if n > 0:
        if n == 1:
            move(src, dest)
        hanoi_rek(n - 1, src, buff, dest)
        move(src, dest)
        hanoi_rek(n - 1, buff, dest, src)
    print(f"""Rekurencyjnie:
    Source: {src}
    Buffer: {buff}
    Destination: {dest}""")

source_r = [4,3,2,1]
buffer_r = []
destination_r = []

source_i = [4,3,2,1]
buffer_i = []
destination_i = []


start = t.time()
steps_iter = hanoi_iter(source_i, destination_i, buffer_i)
time_iter = t.time() - start

start = t.time()
hanoi_rek(4, source_r, destination_r, buffer_r)
time_rek = t.time() - start

print("Ilość kroków iteracyjnie:", steps_iter)
print('Ilość kroków rekurencyjnie:', steps_rek)
print('Czas iteracyjnie:', time_iter)
print('Czas rekurencyjnie:', time_rek)


