'''
(Assign grades) Write a program that reads a list of scores and then assigns grades
based on the following scheme:

The grade is A if score is  >= best - 10.
The grade is B if score is  >= best – 20.
The grade is C if score is  >= best – 30.
The grade is D if score is  >= best – 40.
The grade is F otherwise.
'''

def grades(lst):
    best = int(max(lst))
    m = 0

    while m < len(lst):
        score = int(lst[m])

        if score >=best -10:
            print("Student ", m, " score is ", score, "and grade is A")
        elif score >= best - 20:
            print("Student ", m, " score is ", score, "and grade is B")
        elif score >= best - 30:
            print("Student ", m, " score is ", score, "and grade is c")
        elif score >= best - 40:
            print("Student ", m, " score is ", score, "and grade is D")
        else:
            print("The grade is F otherwise")
        m+=1


def main():
    score = input("Enter scores of students:")
    lst= score.split()
    grades(lst)


main()
