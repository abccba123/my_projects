'''
(Sum elements column by column) Write a function that returns the sum of all the
elements in a specified column in a matrix using the following header:
def sumColumn(m, columnIndex):
Write a test program that reads a 3 x 4 matrix and displays the sum of each column.
'''

def sumColumn(m, col):
    x = 0
    for n in range(len(m)):
        x += m[n][col]
    return x


def main():
    m = []
    for n in range(3):
        print("Enter 3x4 matrix followed by a space for each elements to sum the matrix columns: ", end=" ")
        row = input()
        m.append([float(elem) for elem in row.split(" ")])
    for n in range(len(m[0])):
        print("Sum of the elements for column", n, "is", sumColumn(m, n))


main()

