'''
(Game: learn addition) Write a program that generates two integers under 100 and
prompts the user to enter the sum of these two integers. The program then reports
true if the answer is correct, false otherwise
'''
import random

num1 = random.randint(0, 100)
num2 = random.randint(0, 100)

answer = eval(input("The sum of " + str(num1) + " + " + str(num2) + " is?:"))
print(num1, "+", num2, "=", answer, "is", num1+num2 == answer)
