
import math
amount = eval(input("Enter an investment amount:"))
rate = eval(input("Enter an interest rate:"))
years = eval(input("Enter number of years to invest:"))
rate /= 1200
FutureInvestmentValue = amount * math.pow(1 + rate, years*12)
print("Accumulated value is: ", round(FutureInvestmentValue, 2))
