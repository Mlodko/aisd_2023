import random

def insertionSort(A):
    for i in range(1, len(A)):
        element_to_insert = A[i]
        j = i - 1
        while j >= 0 and A[j] > element_to_insert: 
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = element_to_insert 
    return A
