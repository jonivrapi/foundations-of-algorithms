# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 14:20:03 2022
Modified Sun Sep 4 20 for CLRS 4th Ed

CLRS page 1149 Harmonic Numbers, Splitting Summations
The text develops a bound O(lgn) for the harminic series by splitting
the range 1 to n into floor(lgn) + 1 pieces and upper-bounding the 
contribution of eacch piece by 1.

This program probes the numerical result of each step in Equation A.17.

@author: jboonjr

"""

import math

# Harmonic number
def HarmonicNumber(n):
    Hn = 0
    for k in range(1, n+1):
#        print(k)
        Hn = Hn + (1/k)
    return Hn

def EquationA_17_L1(n):
    Hn = 0
    UL1 = math.floor(math.log2(n))
    UL2 = 2**math.floor(math.log2(n)) - 1
    print("\tUpper Limit Outer Sum:", UL1, "\tUpper Limit Inner Sum:", UL2)
    for i in range(0,UL1+1):
        for j in range(0, 2**i):
            print("\t\ti", i, "j", j,"term",(1/(2**i + j)) )
            Hn = Hn + (1/(2**i + j))
    return Hn
            
def EquationA_17_L2(n):
    Hn = 0
    UL1 = math.floor(math.log2(n))
    for i in range(0,UL1+1):
        for j in range(0, 2**i):
 #           print("i", i, "j", j)
            Hn = Hn + (1/(2**i))
    return Hn

def EquationA_17_L4(n):
    Hn = 0
    UL1 = math.floor(math.log2(n))
    for i in range(0,UL1+1):
        Hn = Hn + 1
    return Hn            

n=int(input("Enter integer for Harmonic Number computation: "))

print("Standard Computation: ", HarmonicNumber(n))
print("Equation A.17, line 1:", EquationA_17_L1(n))
print("Equation A.17, line 2:", EquationA_17_L2(n))
print("Equation A.17, line 4:", EquationA_17_L4(n))
print("Equation A.17, line 5:", math.log2(n)+1)

