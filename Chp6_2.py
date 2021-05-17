def sumDigits(n):
    sum = 0
    while (n != 0):
        sum = sum + int(n%10)
        n = int(n/10)

    return sum


Addition = eval(input("Enter an integer to sum: "))
print("The sum of digits", Addition, "is: ", sumDigits(Addition))
