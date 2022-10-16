from sympy import *

def divideAndConquor(inA, inB, inC, inD): 
    a, b, c, d, n = symbols('a b c d n') 
    
    for i in range(4):
        if (i == 0):
            recursiveCost = n

            if (inC == 1 and inD == 1):
                nonRecursiveCost = 1
            else: 
                nonRecursiveCost = (c*n**d).subs([(d, inD)])

            print(f"At depth {i}, recursive cost is: {recursiveCost}, and non-recursive cost is: {nonRecursiveCost}")
        else:
            recursiveCost = (n/(b**i)).subs(b, inB)

            if (inC == 1 and inD == 1):
                nonRecursiveCost = inA ** i
            else:
                nonRecursiveCost = (a**i).subs(a, inA)*(c*(recursiveCost**d)).subs([(c, inC), (d, inD)])
            
            print(f"At depth {i}, recursive cost is: {recursiveCost}, and non-recursive cost is: {nonRecursiveCost}")

# divideAndConquor(8, 2, 1, 1)
# divideAndConquor(7, 2, 1, 2)
divideAndConquor(3, 4, 1, 2)