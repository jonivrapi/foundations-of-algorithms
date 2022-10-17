from sympy import *

def printResults(index, recursiveCost, nonRecursiveCost, numNodes):
    print(f"At depth {index}, The complete node form is: [T({recursiveCost}) | {nonRecursiveCost}]")
    print(f"The number of nodes at this level is: {numNodes}")
    print(f"The total nonrecursive cost at this level is {simplify(numNodes * nonRecursiveCost)} | or in expanded form {expand(numNodes * nonRecursiveCost)}\n")

def printMessageAndParameters(message, inA, inB, inC, inD):
    print(message)
    print(f"Parameters chosen: {{ a: {inA}, b: {inB}, c: {inC}, d: {inD} }}")
    print('----------------------------')