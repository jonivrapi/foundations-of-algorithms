

loopIterations = 0

def QuickSort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        QuickSort(A, p, q - 1)
        QuickSort(A, q + 1, r)

def Partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        global loopIterations 
        loopIterations += 1
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]

    return i + 1


A = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
p = 0
r = len(A) - 1

QuickSort(A, p, r)

print(A)
print(f'loop iterations: {loopIterations}')