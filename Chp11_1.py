
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

