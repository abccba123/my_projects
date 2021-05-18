'''
(Find future dates) Write a program that prompts the user to enter an integer for
today’s day of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6). Also
prompt the user to enter the number of days after today for a future day and display
the future day of the week
'''
DaysOfWeek = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}

today = int(input("Enter an integer for today's date:"))
future = int(input("Enter the number of days elapsed since today:"))
print('Today is {} and the future day is {}.'.format(DaysOfWeek[today],
                                                     DaysOfWeek[(today+future)%7]))
