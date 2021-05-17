import math

print("Enter the three points of a triangle followed by a space")
x1, y1, x2, y2, x3, y3 = map(float, input().split())
print("The points entered are: ", x1, y1, x2, y2, x3, y3)


side1 = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

side2 = math.sqrt(math.pow(x2 - x3, 2) + math.pow(y2 - y3, 2))

side3 = math.sqrt(math.pow(x1 - x3, 2) + math.pow(y1 - y3, 2))

s = (side1 + side2 + side3) / 2

area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

print("The area of a triangle is: ", round(area, 3))
