'''
(Largest rows and columns) Write a program that randomly fills in 0s and 1s into
a  4x4 matrix, prints the matrix, and finds the rows and columns with the most
1s.
'''

import random
matrix = []
for row in range(4):
    matrix.append([])
    for column in range(4):
        matrix[row].append(random.randint(0, 1))
print(matrix)

maxRow = sum(matrix[0])
indexOfMaxRow = 0
for row in range(1, len(matrix)):
    if sum(matrix[row]) > maxRow:
        maxRow = sum(matrix[row])
        indexOfMaxRow = row
print("The largest row index is:", indexOfMaxRow)

maxColumn = sum(matrix[0])
indexOfMaxColumn = 0
for column in range(1, len(matrix)):
    if sum(matrix[column]) > maxColumn:
        maxColumn = sum(matrix[column])
        indexOfMaxColumn = column
print("The largest column index is:", indexOfMaxColumn)
