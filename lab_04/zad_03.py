from zad_01 import insertionSort
from zad_02 import mergeSort
import time as t
import random
from copy import deepcopy as dc

def generateRandomArray(length):
    arr = []
    for _ in range(length):
        while True:
            to_add = random.randint(1,length)
            if to_add in arr:
                continue
            else:
                arr.append(to_add)
                break
    return arr

def avg(list):
    return sum(list) / len(list)

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    print ("\033[A                             \033[A")
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

iterations = 1000
array_length = 200
insertion_times = []
merge_times = []

printProgressBar(0, iterations)
for i in range(iterations):
    printProgressBar(i, iterations)
    arr1 = generateRandomArray(array_length)
    arr2 = dc(arr1)

    start_time = t.time()
    insertionSort(arr1)
    insertion_times.append(t.time() - start_time)

    start_time = t.time()
    mergeSort(arr2, 0, array_length - 1)
    merge_times.append(t.time() - start_time)

print(f"""Czas wykonania wszystkich iteracji:
    Insertion Sort: {sum(insertion_times)} s
    Merge Sort: {sum(merge_times)} s
    Stosunek Insertion/Merge: {sum(insertion_times) / sum(merge_times)}\n""")
print(f"""Najszybsza iteracja:
    Insertion Sort: {min(insertion_times)} s
    Merge Sort: {min(merge_times)} s 
    Stosunek Insertion/Merge: {min(insertion_times) / min(merge_times)}\n""")
print(f"""Najwolniejsza iteracja:
    Insertion Sort: {max(insertion_times)} s
    Merge Sort: {max(merge_times)} s
    Stosunek Insertion/Merge: {max(insertion_times) / max(merge_times)}\n""")
print(f"""Średni czas wykonania:
    Insertion Sort: {avg(insertion_times)} s
    Merge Sort: {avg(merge_times)} s
    Stosunek Insertion/Merge: {avg(insertion_times) / avg(merge_times)}\n""")