'''
(Reverse number) Write a program that prompts the user to enter a four-digit integer
and displays the number in reverse order.
'''
number = int(input("Enter a 4 digit integer: "))
print("The reversed number is:", int(str(number)[::-1]))
