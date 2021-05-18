''''
Write a program that prompts the user to enter an amount (e.g., 100), the annual
interest rate (e.g., 5), and the number of months (e.g., 6), and displays the amount
in the savings account after the given month.
''''
principal = int(input("Enter an amount: "))
print("Enter the rate: ")
rate = int(input())
print("Enter the number of months")
months = int(input())
amount = 0
x = rate/12
n = 1
print("Month\tSavings Amount")
while n < months:
    n += 1
amount = amount + principal
amount = amount * (1 + x/100)
print(n, "\t", amount)
print("The amount in Savings is: " + str(amount) + " after " + str(months) + " months")

