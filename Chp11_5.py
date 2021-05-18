'''
(Algebra: add two matrices) Write a function to add two matrices. The header of
the function is:
def addMatrix(a, b)
'''

rows = int(input("Enter the number of rows:"))
columns = int(input("Enter the number of columns:"))

print("Enter elements for matrix 1:")
matrix_a = [[float(input()) for i in range(columns)] for i in range(rows)]
print("MAtrix 1 is: ")
for n in matrix_a:
    print(n)

print("Enter elements for matrix 2: ")
matrix_b = [[float(input()) for i in range(columns)] for i in range(rows)]
print("MAtrix 2 is: ")
for n in matrix_b:
    print(n)
result = [[0 for i in range(columns)] for i in range(rows)]

for i in range(rows):
    for j in range(columns):
        result[i][j] = matrix_a[i][j] + matrix_b[i][j]

print("The matrices are added as follows: ")
for r in result:
    print(r)
