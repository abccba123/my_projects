'''
(Sort three numbers) Write the following function to display three numbers in
increasing order:
def displaySortedNumbers(num1, num2, num3):
Write a test program that prompts the user to enter three numbers and invokes the
function to display them in increasing order.
'''

def displaySortedNumbers(num1, num2, num3):
    print("The sorted numbers are: ")
    if float(num1) > float(num2) and float(num1) > float(num3):
        if float(num2) > float(num3):
            print(num3, num2, num1)
        else:
            print(num2, num3, num1)
    elif float(num2) > float(num1) and float(num2) > float(num3):
        if float(num1) > float(num3):
            print(num3, num1, num2)
        else:
            print(num1, num3, num2)
    else:
        if float(num1) > float(num2):
            print(num2, num1, num3)
        else:
            print(num1, num2, num3)


def main():
    print("Enter three numbers:")
    num1 = input()
    num2 = input()
    num3 = input()
    displaySortedNumbers(num1, num2, num3)
main()
