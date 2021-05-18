'''
(Geometry: display angles) Rewrite Listing 2.9, ComputeDistance.py, using the
following function for computing the distance between two points.
def distance(x1, y1, x2, y2):
'''
import math
def distance(x1, y1, x2, y2):
    distance = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
    return distance


x1, y1 = eval(input("Enter the fist point in (x1, y1) format: "))
x2, y2 = eval(input("Enter the second point in (x2, y2) format: "))
print("The distance between the two point is: ", distance(x1, y1, x2, y2))
