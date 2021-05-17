import time

z = time.time()
x = round(z % 26) + 64
print("A random uppercase letter through the time function is:", chr(x))
