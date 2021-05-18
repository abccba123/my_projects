'''
(Count the letters in a string) Write a function that counts the number of letters in
a string using the following header:
def countLetters(s):
Write a test program that prompts the user to enter a string and displays the number
of letters in the string.
'''

def countLetters(s):
    return len(s)


s = input("Enter a string: ")
print("Number of letters in a string:", countLetters(s))
