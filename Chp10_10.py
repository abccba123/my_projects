'''
(Reverse a list) The reverse function in Section 10.8 reverses a list by copying it
to a new list. Rewrite the function that reverses the list passed in the argument and
returns this list. Write a test program that prompts the user to enter a list of numbers,
invokes the function to reverse the numbers, and displays the numbers.
'''

def main():
    revlst = input("Enter the list of numbers to reverse:")
    elem = revlst.split()
    nums = [eval(n) for n in elem]
    reversed(nums)
    print(nums)


def reverse(lst):
    for i in range(len(lst)//2):
        lst[i]
        lst[len(lst) - i -1] = lst[len(lst) - i -1]
        lst[i]
        return lst


main()
