'''
(Compute the weekly hours for each employee) Suppose the weekly hours for all
employees are stored in a table. Each row records an employee’s seven-day work
hours with seven columns. For example, the following table stores the work hours
for eight employees. Write a program that displays employees and their total hours
in decreasing order of the total hours.
'''

Employee = ["Employee 0", "Employee 1", "Employee 2", "Employee 3", "Employee 4", "Employee 5", "Employee 6",
            "Employee 7"]
Employee_hours = [[2, 4, 3, 4, 5, 8, 8],
                  [7, 3, 4, 3, 3, 4, 4],
                  [3, 3, 4, 3, 3, 2, 2],
                  [9, 3, 4, 7, 3, 4, 1],
                  [3, 5, 4, 3, 6, 3, 8],
                  [3, 4, 4, 6, 3, 4, 4],
                  [3, 7, 4, 8, 3, 8, 4],
                  [6, 3, 5, 9, 2, 7, 9]]

employee_lst = len(Employee_hours)
answer = []
for m in range(employee_lst):
    Total_Hours = sum(Employee_hours[m])
    answer.append([Total_Hours, Employee[m]])
answer.sort(reverse=True)

print("The result in the Decreasing order of Total hours is")
print('Employees', 'Total_Hours')
for i in answer:
    print(i[1], i[0])
