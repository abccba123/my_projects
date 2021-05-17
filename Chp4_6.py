intWeight = eval(input("Enter weight in pounds: "))
intFeet = eval(input("Enter feet: "))
intInches = eval(input("Enter inches: "))
floatHeight = (intFeet*12) + intInches
bmi = (intWeight/floatHeight**2)*703
print("Bmi is:", bmi)
if bmi < 18.5:
    print("You are Underweight")
elif bmi < 25:
    print("You are Normal")
elif bmi < 30:
    print("You are overweight")
print()