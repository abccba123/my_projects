'''
(Display four patterns using loops) Use nested loops that display the following
patterns in four separate programs:
Pattern A      Pattern B       Pattern C       Pattern D
1              1 2 3 4 5 6             1       1 2 3 4 5 6
1 2            1 2 3 4 5             2 1       1 2 3 4 5
1 2 3          1 2 3 4             3 2 1       1 2 3 4
1 2 3 4        1 2 3             4 3 2 1       1 2 3
1 2 3 4 5      1 2             5 4 3 2 1       1 2
1 2 3 4 5 6    1             6 5 4 3 2 1       1
'''
print("Pattern A")
for m in range(1,7):
    for n in range(1, m+1):
        print(n, end=' ')
    print("")

print("Pattern B")
for m in range(6, 0, -1):
    for n in range(1, m+1):
        print(n, end=' ')
    print("")

print("Pattern C")
for m in range(1, 6+1):
    for n in range(6, 0, -1):
        print(n if n < m else " ", end=' ')
    print()

print("Pattern D")
for m in range(6, 0, -1):
    for n in range(1, m+1):
        print(n, end=' ')
    print("")

