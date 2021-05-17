
print("Enter the subtotal and the gratuity rate in percentage: ")
subtotal = eval(input())
gratuity = eval(input())
# formula to calculate gratuity and total using input
gratuity = (subtotal*gratuity)/100 # divide the gratuity by 100 to convert from percentage to float value
total = subtotal + gratuity

print("The gratuity is:" + str(round(gratuity, 2)) + " and the total is:" + str(round(total, 2)))