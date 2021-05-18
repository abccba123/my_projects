'''
(Turtle: draw the Olympic symbol ) Write a program that prompts the user to
enter the radius of the rings and draws an Olympic symbol of five rings of the
same size with the colors blue, black, red, yellow, and green
'''
import turtle
radius = eval(input("Enter the radius for circle:"))
turtle.pensize(15)

turtle.color("blue")
turtle.penup()
turtle.goto(-110, -25)
turtle.pendown()
turtle.circle(radius)

turtle.pensize(15)
turtle.color("black")
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.circle(radius)

turtle.pensize(15)
turtle.color("red")
turtle.penup()
turtle.goto(110, -25)
turtle.pendown()
turtle.circle(radius)

turtle.pensize(15)
turtle.color("yellow")
turtle.penup()
turtle.goto(-55, -75)
turtle.pendown()
turtle.circle(radius)

turtle.pensize(15)
turtle.color("green")
turtle.penup()
turtle.goto(55, -75)
turtle.pendown()
turtle.circle(radius)
turtle.done()
