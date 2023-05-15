import random

def mergeSort(A, a, b):
    if a < b: 
        middle = (a+b)//2
        mergeSort(A, a, middle)
        mergeSort(A, middle + 1, b)
        merge(A, a, middle, b)
    return A

def merge(arr, l, mid, r):
    n1 = mid - l + 1
    n2 = r - mid 

    Left = [0] * (n1)
    Right = [0] * (n2)

    for i in range(0, n1):
        Left[i] = arr[l + i]
    for i in range(0,n2):
        Right[i] = arr[mid + 1 + i]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if Left[i] <= Right[j]:
            arr[k] = Left[i]
            i += 1
        else:
            arr[k] = Right[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = Left[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k] = Right[j]
        j += 1
        k += 1
