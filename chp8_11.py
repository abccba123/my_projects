'''
(Reverse a string) Write a function that reverses a string. The header of the function
is:
def reverse(s):
Write a test program that prompts the user to enter a string, invokes the reverse
function, and displays the reversed string.
'''

def reverse(s):
    answer = ""
    for m in s:
        answer = m + answer
    return answer

def main():
    n = input("Enter string: ")
    print("Reversed string:",reverse(n))

main()
