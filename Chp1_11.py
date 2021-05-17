currentpopulation = 312032486
print("The current population is:", currentpopulation)

# one birth every 7 seconds =(+1)
# one death every 12 seconds = (-1)
# one new immigrant 45 seconds = (+1)

# 1 min =60 sec, 1 hour = 3600 sec, 1 day = 86400, 1 year = 31,536,000

NumberOfSecondsInADay = 31536000

NumberOfBirthsPerYear = NumberOfSecondsInADay//7
print("The count of births per 1 year is: ", NumberOfBirthsPerYear)

DeathsPerYear = NumberOfSecondsInADay//12
print("The count of Deaths per year is:", DeathsPerYear)

NewImmigrantPerYear = NumberOfSecondsInADay//45
print("The count of new immigrants per year is: ", NewImmigrantPerYear)

# count for a year including births,deaths and immigrants
CountInaYear = NumberOfBirthsPerYear - DeathsPerYear + NewImmigrantPerYear
print("Count for a year is: ", CountInaYear)

# printing the count of births, death and new immigrants after 5 years

print("The count of population in 5 years is:" , currentpopulation + (5*CountInaYear))


