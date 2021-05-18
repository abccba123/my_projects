'''
Write a program that reads the subtotal and
the gratuity rate and computes the gratuity and total. For example, if the user
enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5
as the gratuity and 11.5 as the total.
'''
print("Enter the subtotal and the gratuity rate in percentage: ")
subtotal = eval(input())
gratuity = eval(input())
# formula to calculate gratuity and total using input
gratuity = (subtotal*gratuity)/100 # divide the gratuity by 100 to convert from percentage to float value
total = subtotal + gratuity

print("The gratuity is:" + str(round(gratuity, 2)) + " and the total is:" + str(round(total, 2)))
