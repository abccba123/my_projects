def check_SSN(SSN):
    if len(SSN) == 11:
        if SSN[3] and SSN[6] == '-':
            valid = True
    else:
        valid = False
    return valid


SSN = input("Enter an ssn in the ddd-dd-dddd format:")
print(check_SSN(SSN))


