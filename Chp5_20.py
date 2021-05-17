# incomplete program
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

