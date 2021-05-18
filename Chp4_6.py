'''
(Health application: BMI ) Revise Listing 4.6, ComputeBMI.py, to let users enter
their weight in pounds and their height in feet and inches. For example, if a person
is 5 feet and 10 inches, you will enter 5 for feet and 10 for inches.
'''
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
