import matplotlib.pyplot as plt
import numpy as np
from utils import *
from ProgrammingAssignment1 import *

# setting m modifies how many of the closest pairs are returned
m = 2
numberOfInputs = [5, 10, 50, 100, 200, 500, 1000]
numberOfIterations = []

for n in numberOfInputs:
    points: List[Point] = []
    for i in range(n):
        x: int = random.randint(0, 10000)
        y: int = random.randint(0, 10000)
        points.append(Point(x, y))

    (pairs, length) = mClosestPoints(points, m)
    print(length)
    numberOfIterations.append(length)

plt.scatter(numberOfInputs, numberOfIterations)

plt.xlabel("Number of Inputs")
plt.ylabel("Number of Iterations")

plt.show()

