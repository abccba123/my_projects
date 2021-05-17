import math
def distance(x1, y1, x2, y2):
    distance = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
    return distance


x1, y1 = eval(input("Enter the fist point in (x1, y1) format: "))
x2, y2 = eval(input("Enter the second point in (x2, y2) format: "))
print("The distance between the two point is: ", distance(x1, y1, x2, y2))