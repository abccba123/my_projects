def count(s, ch):
    answer = 0
    for n in range(len(s)):
        if (s[n] == ch):
            answer = answer + 1
    return answer


s = input("Enter a string: ")
ch = input("Enter the character u want to count: ")
print(count(s, ch))