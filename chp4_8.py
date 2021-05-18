'''
(Sort three integers) Write a program that prompts the user to enter three integers
and displays them in increasing order.
'''

print("Enter three integers to sort them in increasing order: ")
num1 = eval(input())
num2 = eval(input())
num3 = eval(input())

if (num1 <= num2) & (num1 <= num3):
    smallest = num1
elif (num2 <= num1) & (num2 <= num3):
    smallest = num2
else:
    smallest = num3
if (num1 >= num2) & (num1 >= num3):
    highest = num1
elif (num2 >= num1) & (num2 >= num3):
    highest = num2
else:
    highest = num3
middle = (num1 + num2 + num3) - highest - smallest
print(highest, middle, smallest)
