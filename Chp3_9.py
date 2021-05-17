# extra space in output solve it
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

