def main():
    lst = input("Enter the list of integers to reverse: ")
    elem = lst.split()
    numbers = [eval(n) for n in elem]
    numbers.reverse()
    print("The reversed list of integers: ", numbers)


main()