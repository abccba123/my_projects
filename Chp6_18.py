import random
def printMatrix(n):
    for m in range(n):
        for i in range(n):
            print(random.randint(0, 1), ' ', end=' ')
        print("\n", end='')
n = int(input("Enter a number to display an nxn matrix: "))


printMatrix(n)
