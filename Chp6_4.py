'''
(Display an integer reversed) Write the following function to display an integer in
reverse order:
def reverse(number):
For example, reverse(3456) displays 6543. Write a test program that prompts
the user to enter an integer and displays its reversal.
'''

def reverse(number):
    while number > 0:
        print(number % 10, end='')
        number //= 10


Reverse = int(input("Enter an integer to reverse: "))
reverse(Reverse)
