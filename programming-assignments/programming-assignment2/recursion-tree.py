from enum import Enum 

class AlgorithmType(Enum):
    DIVIDE_AND_CONQUER = 1
    CHIP_AND_BE_CONQUERED = 2

class AlgorithmInput:
    def __init__(self, type: AlgorithmType, a, b, c, d, e):
        self.type = type
        self.a = a
        self. b = b
        self.c = c
        self.d = d
        self.e = e
       

algo_input = input("Press 1 for Divide and Conquer, 2 for Chip and Be Conquered")


