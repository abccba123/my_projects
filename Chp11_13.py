'''
(Locate the largest element) Write the following function that returns the location
of the largest element in a two-dimensional list:
def locateLargest(a)
'''

def locateLargest(a):
    RLargestIndex, CLargestIndex = 0,0
    for m in range(len(a)):
        for n in range(len(a[m])):
            if a[m][n] > a[RLargestIndex][CLargestIndex]:
                RLargestIndex, CLargestIndex = m, n
    return RLargestIndex, CLargestIndex


def main():
    matrix = []
    row_input = int(input("Enter the number of rows: "))
    for m in range(row_input):
        matrix.append([float(b.strip()) for b in input("Enter row: ").split()])
    k, l = locateLargest(matrix)
    print("The location of the largest element is at ({},{})".format(k, l))


main()
