import math

def QuickSort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        QuickSort(A, p, q - 1)
        QuickSort(A, q + 1, r)

def Partition(A, p, r):
    i = p - 1
    j = p

    if j - i >= 2:
        x = MedianOfThree(A, p, r)
    else:
        x = A[r]

    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]

    return i + 1

def MedianOfThree(A, i, j):
    k = math.floor((i + j) / 2)

    tempArray = [A[i], A[k], A[j]]
    tempArray.sort()
    
    medianIndex = 1
    
    return tempArray[medianIndex]
    


A = [1, 9, 2, 8, 5, 3, 7, 6, 4, 4, 4]
p = 0
r = len(A) - 1

QuickSort(A, p, r)

print(A)