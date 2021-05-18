'''
(Find the highest score) Write a program that prompts the user to enter the number
of students and each student’s score, and displays the highest score. Assume that
the input is stored in a file named score.txt, and the program obtains the input from
the file.
'''
# creating an empty list
lst = []

n = int(input("Enter number of students : "))
print("Enter the score and then press enter to input the next score: ")

for i in range(0, n):
    scores = int(input())

    lst.append(scores)

print(lst)

print(max(lst))
