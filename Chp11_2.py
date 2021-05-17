def main():
    matrix = []

    for i in range(1,5):
        a = input("Enter a 4x4 matrix row " + str(i) + ": ")
        items = a.split()
        list = [eval (x) for x in items]
        matrix.append(list)

    print("Sum of the elements in the major diagonal is:", sumMajorDiagonal(matrix))


def sumMajorDiagonal(m):
    sum = 0
    for i in range(len(m)):
        sum += m[i][i]
    return sum

main()