import math
import random

loopIterations = 0

def QuickSort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        QuickSort(A, p, q - 1)
        QuickSort(A, q + 1, r)

def Partition(A, p, r):
    i = p - 1

    (pivotValue, pivotIndex) = MedianOfThree(A, p, r)
    # The book's implementation of Partition requires the partition on the right, so I swap the pivot with that here
    A[r], A[pivotIndex] = A[pivotIndex], A[r]

    for j in range(p, r):
        global loopIterations 
        loopIterations += 1
        if A[j] <= pivotValue:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]

    return i + 1

def MedianOfThree(A, p, r):
    k = math.floor((p + r) / 2)

    #sorted runs in O(n) in this case
    tempArray = sorted([(A[p], p), (A[k], k), (A[r], r)], key=lambda tup: tup[0])

    medianIndex = 1

    if r - p >= 2:
        return tempArray[medianIndex]
    else:
        return (A[r], r)
    
    

for i in range(0, 10):
    A = sorted([random.random() for _ in range(10)])
    A.reverse()
    p = 0
    r = len(A) - 1

    QuickSort(A, p, r)

    print(A)
    print(f'loop iterations: {loopIterations}')
    loopIterations = 0