import math
# Object that represents a point in 2d space with an x and y coordinate.
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def toString(self):
        return f"Point: ({self.x}, {self.y})"

# Object that represents a pair of points, and their distance
class Pair:
    def __init__(self, pointA: Point, pointB: Point, distance: float):
        self.pointA = pointA
        self.pointB = pointB
        self.distance = distance

    def toString(self):
        return f"PointA: ({self.pointA.x}, {self.pointA.y}) | PointB: ({self.pointB.x}, {self.pointB.y}). Distance between the points: {self.distance}"

# Utility method that calculates the Euclidean distance between two points
def euclideanDistance(pointA: Point, pointB: Point):
    xDifference = pointA.x - pointB.x
    yDifference = pointA.y - pointB.y

    xDifferenceSquared = pow(xDifference, 2)
    yDifferenceSquared = pow(yDifference, 2)
    
    return math.sqrt(xDifferenceSquared + yDifferenceSquared)