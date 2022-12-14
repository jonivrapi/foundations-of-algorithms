from sympy import *
from utils import *

def divideAndConquer(inA, inB, inC, inD, message):
    # i specifically do not check for c being strictly > 0 because i use the combination of c and d as zero to indicate that its a constant function
    if inA < 1 or inB <= 1 or not isinstance(inB, Rational) or inC < 0 or inD < 0 or not isinstance(inC, Rational) or not isinstance(inD, Rational):
        raise ValueError("Your parameters do not fit the criteria")

    printMessageAndParameters(message, inA, inB, inC, inD)
    
    # Declare symbols for each variable
    a, b, c, d, n = symbols('a b c d n') 
    
    iterationCount = 0
    for i in range(4):
        iterationCount += 1
        # starting case
        if (i == 0):
            recursiveCost = n
            numNodes = 1

            # When you choose your input for c and d to be zero, I use this to signify that the f(n) term is a constant
            if (inC == 0 and inD == 0):
                # If c = 0 and d = 0 are chose, f(n) is a constant 1
                nonRecursiveCost = 1
            else: 
                # The non recursive cost is calculated as cn^d
                nonRecursiveCost = (c*n**d).subs([(c, inC), (d, inD)])

            printResults(i, recursiveCost, nonRecursiveCost, numNodes)
        # depth > 0 cases
        else:
            # recursive cost is calculated as n/(b^i)
            recursiveCost = (n/(b**i)).subs(b, inB)
            # number of nodes at a level is calculated as a^i where i is the current depth of the tree
            numNodes = (a**i).subs(a, inA)

            # when you choose your input for c and d to be zero, i use this to signify the f(n) ter is a constant
            if (inC == 0 and inD == 0):
                # If c = 0 and d = 0 are chose, f(n) is a constant 1
                nonRecursiveCost = 1
            else:
                # otherwise it is calculated as the number of nodes * c*recursiveCost^d
                nonRecursiveCost = (c*(recursiveCost**d)).subs([(c, inC), (d, inD)])
            
            printResults(i, recursiveCost, nonRecursiveCost, numNodes)
    return iterationCount
    

divideAndConquer(8, Rational(2), Rational(0), Rational(0), 'Equation 4.9 on page 84')
divideAndConquer(7, Rational(2), Rational(1), Rational(2), 'Equation 4.10 on page 86')
divideAndConquer(3, Rational(4), Rational(1), Rational(2), 'Figure 4.1 on page 96')