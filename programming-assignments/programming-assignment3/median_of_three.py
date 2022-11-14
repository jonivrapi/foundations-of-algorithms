import math

loopIterations = 0

def QuickSort(A, lowIndex, highIndex):
    if lowIndex < highIndex:
        q = Partition(A, lowIndex, highIndex)
        QuickSort(A, lowIndex, q - 1)
        QuickSort(A, q + 1, highIndex)

def Partition(A, lowIndex, highIndex):
    i = lowIndex - 1

    (pivotValue, pivotIndex) = MedianOfThree(A, lowIndex, highIndex)
    A[highIndex], A[pivotIndex] = A[pivotIndex], A[highIndex]

    for j in range(lowIndex, highIndex):
        global loopIterations 
        loopIterations += 1
        if A[j] <= pivotValue:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[highIndex] = A[highIndex], A[i + 1]

    return i + 1

def MedianOfThree(A, lowIndex, highIndex):
    k = math.floor((lowIndex + highIndex) / 2)

    #sorted runs in O(n) in this case
    tempArray = sorted([(A[lowIndex], lowIndex), (A[k], k), (A[highIndex], highIndex)], key=lambda tup: tup[0])

    medianIndex = 1

    if highIndex - lowIndex >= 2:
        return tempArray[medianIndex]
    else:
        return (A[highIndex], highIndex)
    
    
    


A = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
p = 0
r = len(A) - 1

QuickSort(A, p, r)

print(A)
print(f'loop iterations: {loopIterations}')