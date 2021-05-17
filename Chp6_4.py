def reverse(number):
    while number > 0:
        print(number % 10, end='')
        number //= 10


Reverse = int(input("Enter an integer to reverse: "))
reverse(Reverse)