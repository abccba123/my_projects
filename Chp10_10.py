
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