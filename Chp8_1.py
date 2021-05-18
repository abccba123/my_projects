'''
(Check SSN) Write a program that prompts the user to enter a Social Security
number in the format ddd-dd-dddd, where d is a digit. The program displays
Valid SSN for a correct Social Security number or Invalid SSN otherwise.
✓Point Check
'''
def check_SSN(SSN):
    if len(SSN) == 11:
        if SSN[3] and SSN[6] == '-':
            valid = True
    else:
        valid = False
    return valid


SSN = input("Enter an ssn in the ddd-dd-dddd format:")
print(check_SSN(SSN))


