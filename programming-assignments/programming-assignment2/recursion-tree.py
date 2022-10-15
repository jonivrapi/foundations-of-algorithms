from enum import Enum 

class Node: 
    def __init__(self, size, nonRecursiveCost) -> None:
        self.size = size
        self.nonRecursiveCost = nonRecursiveCost

class AlgorithmType(Enum):
    DIVIDE_AND_CONQUER = 1
    CHIP_AND_BE_CONQUERED = 2

class AlgorithmInput:
    # def __init__(self, type: AlgorithmType, a, b, c, d, e):
    #     self.type = type
    #     self.a = a
    #     self. b = b
    #     self.c = c
    #     self.d = d
    #     self.e = e
    def __init__(self) -> None:
        pass
    
    def askForInput(self) -> None:
        self.type = int(input('Press 1 for Divide and Conquer, 2 for Chip and Be Conquered: '))
        self.a = input('Enter a value for a: ')
        self.b = input('Enter a value for b: ')
        self.c = input('Enter a value for c: ')
        self.d = input('Enter a value for d: ')

    def toString(self) -> None:
        print(f"Chosen Algorithm type: {AlgorithmType(self.type).name} -> {{ a: {self.a}, b: {self.b}, c: {self.c}, d: {self.d}}}")
       

# algo_input = int(input("Press 1 for Divide and Conquer, 2 for Chip and Be Conquered: "))
# print(AlgorithmType(algo_input).name)

algorithmInput = AlgorithmInput()
algorithmInput.askForInput()
algorithmInput.toString()

