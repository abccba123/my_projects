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
