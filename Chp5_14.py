'''
(Find the smallest n such that n2 12,000) Use a while loop to find the smallest
integer n such that n2 is greater than 12,000.
'''

# Use a while loop to find the smallest
# integer n such that n2 is greater than 12,000.
n = 1
while n*n <= 12000:
    n += 1
print(str(n))
