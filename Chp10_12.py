'''
(Compute GCD) Write a function that returns the greatest common divisor
(GCD) of integers in a list. Use the following function header:
def gcd(numbers):
Write a test program that prompts the user to enter five numbers, invokes the
function to find the GCD of these numbers, and displays the GCD.
'''

def gcd(numbers):
    answer = numbers[0]
    for m in numbers[1:]:
        x = answer
        y = m
        while y >0:
            x, y =y, x%y

        answer = x

    return answer


def main():
    numbers = []
    print("Enter 5 numbers and press enter after entering each number to find GCD:")
    for i in range(0, 5):
        elem = int(input())
        numbers.append(elem)


    answer = gcd(numbers)
    print("The GCD is: ", answer)


main()
