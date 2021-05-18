'''
(Display matrix of 0s and 1s) Write a function that displays an n-by-n matrix using
the following header:
def printMatrix(n):
Each element is 0 or 1, which is generated randomly. Write a test program that
prompts the user to enter n and displays an n-by-n matrix.
'''

import random
def printMatrix(n):
    for m in range(n):
        for i in range(n):
            print(random.randint(0, 1), ' ', end=' ')
        print("\n", end='')
n = int(input("Enter a number to display an nxn matrix: "))


printMatrix(n)
