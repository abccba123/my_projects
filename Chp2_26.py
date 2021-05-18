'''
(Turtle: draw a circle) Write a program that prompts the user to enter the
center and radius of a circle, and then displays the circle and its area
'''
import turtle
import math
m, n = eval(input("Enter the center for the circle"))
radius = eval(input("Enter the radius for the circle"))

turtle.penup()
turtle.goto(m, n - radius)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.hideturtle()
turtle.goto(m, n)
turtle.write(math.pi * radius **2)
turtle.done()
