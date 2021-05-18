'''
(Longest common prefix) Write a method that returns the longest common prefix
of two strings. For example, the longest common prefix of distance and
disinfection is dis. The header of the method is:
def prefix(s1, s2)
If the two strings have no common prefix, the method returns an empty string.
Write a main method that prompts the user to enter two strings and displays their
common prefix.
'''

def prefix(s1, s2):
    m =0
    n =0
    s = ""
    com = ""

    while m < len(s1) and n < len(s2):

         if s1[m] == s2[m]:
            s = s + s1[m]
            m+= 1
            n+= 1
         else:

            if len(s1) < len(s2):
                m+=0
                n+=1
            else:

             n +=0
             m+=1
             s = ""

            if len(com) < len(s):
             com = s
    return com


def main():
    s1 = input("Enter string 1 here: ")
    s2 = input("Enter string 2 here: ")
    print("The longest common prefix is:", prefix(s1, s2))


main()

