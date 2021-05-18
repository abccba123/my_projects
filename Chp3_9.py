'''
(Financial application: payroll) Write a program that reads the following information
and prints a payroll statement:
Employee’s name (e.g., Smith)
Number of hours worked in a week (e.g., 10)
Hourly pay rate (e.g., 9.75)
Federal tax withholding rate (e.g., 20%)
State tax withholding rate (e.g., 9%)
'''

a = input("Enter employee's name:")
b = eval(input("Enter the number of hours worked in a week:"))
c = eval(input("Enter hourly pay rate:"))
e = eval(input("Enter federal tax withholding rate:"))
f = eval(input("Enter state tax withholding rate:"))
floatgrosspay = b*c
floatfederalwithholding = (floatgrosspay*e) / 100
floatstatetaxwithholding = (floatgrosspay*f) / 100
floatTotalDeduction = floatfederalwithholding+floatstatetaxwithholding
floatNetPay = floatgrosspay-floatTotalDeduction
print("Employee name:", a)
print("hours worked:", b)
print("Pay rate:","$",c)
print("Deductions:")
print("     Federal Withholding","(",e,"%)", floatfederalwithholding)
print("     state withholding","(",f,"&)", floatstatetaxwithholding)
print("     Total Deduction:","$",floatTotalDeduction)
print("Net pay: ","$",floatNetPay)

