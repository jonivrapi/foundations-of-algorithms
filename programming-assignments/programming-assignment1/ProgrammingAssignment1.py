from typing import List
from utils import *
import random

points: List[Point] = []
length = 0
# setting n modifies how many points are generated
n = 10
# setting m modifies how many of the closest pairs are returned
m = 5

# algorithm that checks each point against every other point, not including itself or previously checked points, then populates an array with the pairs, and sorts them by distance, returning the m closest pairs. 
def mClosestPoints(points: List[Point], m: int):
    if m > len(points):
        raise ValueError('You have chosen an m that is too large given the length of the list of points.')
    elif m < 0:
        raise ValueError('You cannot choose an m less than zero.')

    pairs = []
    pointA = None
    pointB = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            pointA = points[i]
            pointB = points[j]
            distance = euclideanDistance(pointA, pointB)
            
            pairs.append(Pair(pointA, pointB, distance))

    # python's sorted() uses timsort, which is nlogn worst-case
    pairs = sorted(pairs, key=lambda pair: pair.distance)
    # because the pairs array is populated on each iteration of the inner loop, its length represents the number of times this function has iterated
    length = len(pairs)
    
    return pairs[:m], length

# -- Driver code --

for i in range(n):
    x: int = random.randint(0, 10000)
    y: int = random.randint(0, 10000)
    points.append(Point(x, y))

(pairs, length) = mClosestPoints(points, m)
print(f"Total Iterations: {length}")

for i in range(len(pairs)):
    print(pairs[i].toString())

