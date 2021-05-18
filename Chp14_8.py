'''
(Display nonduplicate words in ascending order) Write a program that prompts
the user to enter a text file, reads words from the file, and displays all the nonduplicate
words in ascending order.
'''

print("Enter a text file name: ")
file_input = input()
try:
    file = open("")
    words = []
    for m in file:
        words = m.strip().split("")
    words = list((set(words)))
    words.sort()
    print(words)
    file.close()

except FileNotFoundError:
    print("text file is not in working directory")
