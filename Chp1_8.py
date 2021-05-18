'''
Write a program that displays the area and
perimeter of a circle that has a radius of 5.5 using the following formulas:
'''
import math
r = 5.5
# formula for finding area and perimeter
area = r*r*math.pi
perimeter = 2*r*math.pi
print(round(area, 4))
print(round(perimeter, 4))

