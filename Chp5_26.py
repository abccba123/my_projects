Sum = 0.0
m = 1
n = 1
for m in range(1, 99, 2):
    n = m + 2
    print(m, "/", n, "+", end=' ')
    Sum = Sum + (m/n)
print()
print("Sum = ", round(Sum, 4))