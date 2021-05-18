'''
(Reverse the numbers entered) Write a program that reads a list of integers and
displays them in the reverse order in which they were read.
'''

def main():
    lst = input("Enter the list of integers to reverse: ")
    elem = lst.split()
    numbers = [eval(n) for n in elem]
    numbers.reverse()
    print("The reversed list of integers: ", numbers)


main()
