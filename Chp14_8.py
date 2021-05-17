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
