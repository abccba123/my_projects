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