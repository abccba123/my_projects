def reverse(s):
    answer = ""
    for m in s:
        answer = m + answer
    return answer

def main():
    n = input("Enter string: ")
    print("Reversed string:",reverse(n))

main()