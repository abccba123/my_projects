DaysOfWeek = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}

today = int(input("Enter an integer for today's date:"))
future = int(input("Enter the number of days elapsed since today:"))
print('Today is {} and the future day is {}.'.format(DaysOfWeek[today],
                                                     DaysOfWeek[(today+future)%7]))