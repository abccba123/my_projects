'''
(Sum a series) Write a program to sum the following series:
1/3 + 3/5 + 5/7 + 7/9 + 9/11 + 11/13 + ..... + 97/99
'''
Sum = 0.0
m = 1
n = 1
for m in range(1, 99, 2):
    n = m + 2
    print(m, "/", n, "+", end=' ')
    Sum = Sum + (m/n)
print()
print("Sum = ", round(Sum, 4))
