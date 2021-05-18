''''
(Count single digits) Write a program that generates 1,000 random integers
between 0 and 9 and displays the count for each number. (Hint: Use a list of ten
integers, say counts, to store the counts for the number of 0s, 1s, ..., 9s.)
'''

import random
Count0 = 0
Count1 = 0
Count2 = 0
Count3 = 0
Count4 = 0
Count5 = 0
Count6 = 0
Count7 = 0
Count8 = 0
Count9 = 0
m = 0

while m < 1000:
    x = (random.randint(0, 9))
    m += 1

    if x == 0:
        Count0 = Count0 + 1
    elif x == 1:
        Count1 = Count1 + 1
    elif x == 2:
        Count2 = Count2 + 1
    elif x == 3:
        Count3 = Count3 + 1
    elif x == 4:
        Count4 = Count4 + 1
    elif x == 5:
        Count5 = Count5 + 1
    elif x == 6:
        Count6 = Count6 + 1
    elif x == 7:
        Count7 = Count7 + 1
    elif x == 8:
        Count8 = Count8 + 1
    elif x == 9:
        Count9 = Count9 + 1

print("Count 0: ", Count0)
print("Count 1: ", Count1)
print("Count 2: ", Count2)
print("Count 3: ", Count3)
print("Count 4: ", Count4)
print("Count 5: ", Count5)
print("Count 6: ", Count6)
print("Count 7: ", Count7)
print("Count 8: ", Count8)
print("Count 9: ", Count9)
