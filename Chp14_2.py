'''
(Count occurrences of numbers) Write a program that reads an unspecified number
of integers and finds the ones that have the most occurrences. For example, if
you enter 2 3 40 3 5 4 –3 3 3 2 0, the number 3 occurs most often. Enter all numbers
in one line. If not one but several numbers have the most occurrences, all of
them should be reported. For example, since 9 and 3 appear twice in the list 9 30
3 9 3 2 4, both occurrences should be reported.
'''

number_input = list(map(int , input("Enter an unspecified numbers of integers: ").split()))
freq_lst={}
freq_count = 0
for i in number_input:
    if i not in freq_lst.keys():
        freq_lst[i] = number_input.count(i)
        if freq_lst[i] > freq_count:
            freq_count = freq_lst[i]


print("number with frequent counts: ", freq_lst)
for i in freq_lst.keys():
    if freq_lst[i] == freq_count:
        print("number with most occurrences is: ",i)
print("the count of number(s)", freq_lst, "is: ", freq_count)
