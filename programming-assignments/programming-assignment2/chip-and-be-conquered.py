from sympy import *

def chipAndBeConquered(inA, inB, inC, inD, message):
    # i specifically do not check for c being strictly > 0 because i use the combination of c and d as zero to indicate that its a constant function
    if inA < 1 or inB <= 1 or type(inA) is not int or type(inB) is not int or inC < 0 or inD < 0 or not isinstance(inC, Rational) or not isinstance(inD, Rational):
        raise ValueError("Your parameters do not fit the criteria")
    print(message)
    print(f"Parameters chosen: {{ a: {inA}, b: {inB}, c: {inC}, d: {inD}}}")
    print('----------------------------')
    
    a, b, c, d, n = symbols('a b c d n') 
    
    for i in range(4):
        # starting case
        if i == 0:
            recursiveCost = n

            # when you choose your input for c and d to be zero, i use this to signify the f(n) ter is a constant
            if inC == 0 and inD == 0:
                # If c = 0 and d = 0 are chose, f(n) is a constant starting at 1
                nonRecursiveCost = 1
            else: 
                # the non recursive cost is calculated as cn^d
                nonRecursiveCost = (c*n**d).subs([(c, inC), (d, inD)])
            
            print(f"At depth {i}, recursive cost is: {recursiveCost}, and non-recursive cost is: {nonRecursiveCost}")
            print(f"The complete node form is: {inA}T({recursiveCost}) + {nonRecursiveCost}")
            print("The number of nodes at this level is: 1\n")
        # depth > 0 cases
        else:
            #r recursive cost is calculated as n-b*i
            recursiveCost = (n - b*i).subs(b, inB)
            # number of nodes at a level is calculated as a^i where i is the current depth of the tree
            numNodes = (a**i).subs(a, inA)

            if inC == 0 and inD == 0:
                # outside of the starting case, when referring to a constant f(n), the non-recursive cost is calculated as a^i where i is current depth of tree
                nonRecursiveCost = (a ** i).subs(a, inA)
            else:
                # otherwise it is calculated as c(n-b*i)^d
                nonRecursiveCost = (c*((n - b*i).subs(b, inB))**d).subs([(c, inC), (d, inD)])
        
            
            print(f"At depth {i}, recursive cost is: {recursiveCost}, and non-recursive cost is: {nonRecursiveCost}")
            print(f"The complete node form is: {inA}T({recursiveCost}) + {nonRecursiveCost}")
            print(f"The number of nodes at this level is: {numNodes}\n")



chipAndBeConquered(1, 1, Rational(1), Rational(1), 'Problem 4.3-1 (a) on page 94')
chipAndBeConquered(2, 1, Rational(0), Rational(0), 'Problem 4.3-3 on page 95')
chipAndBeConquered(1, 2, Rational(1), Rational(2), 'Problem 4-1 (h) on page 119')