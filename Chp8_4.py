'''
(Occurrences of a specified character) Write a function that finds the number of
occurrences of a specified character in a string using the following header:
def count(s, ch):
The str class has the count method. Implement your method without using the
count method. For example, count("Welcome", 'e') returns 2. Write a test
program that prompts the user to enter a string followed by a character and displays
the number of occurrences of the character in the string.
'''
def count(s, ch):
    answer = 0
    for n in range(len(s)):
        if (s[n] == ch):
            answer = answer + 1
    return answer


s = input("Enter a string: ")
ch = input("Enter the character u want to count: ")
print(count(s, ch))
