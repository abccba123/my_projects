scores = input("Enter an unspecified number of scores: ")
n = [int(m) for m in scores.split()]
sum = 0
for i in range(len(n)):
    sum = sum + n[i]
average = sum/float(len(n))
AboveAvg = 0
BelowAvg = 0

for i in range(len(n)):
    if n[i] >= average:
        AboveAvg += 1
    elif n[i] < average:
        BelowAvg += 1

print("Count of Scores that are above average are: ", AboveAvg)
print("Count of Scores that are below average are: ", BelowAvg)