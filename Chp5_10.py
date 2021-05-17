# creating an empty list
lst = []

n = int(input("Enter number of students : "))
print("Enter the score and then press enter to input the next score: ")

for i in range(0, n):
    scores = int(input())

    lst.append(scores)

print(lst)

print(max(lst))