import re

def is_valid_credit_card(cc):
    # Case 1 - It must start with a 4, 5, or 6.
    if(cc[0] != '4' and cc[0] != '5' and cc[0] != '6'):
        return False

    # Case 2 - It must contain exactly 16 digits.
    if(len(cc.replace('-', '')) != 16):
        return False

    d = 0
    for i in range(len(cc)):
        # Check for separators ("-") and ensure they appear at most 3 times consecutively.
        if(cc[i] == '-' and d != 4):
            return False
        elif(cc[i] == '-' and d == 4):
            d = 0
        else:
            d += 1

    for i in range(len(cc)):
        # Check if all non-separator characters are digits.
        if cc[i] == '-':
            continue
        if not cc[i].isdigit():
            return False

    # Check for invalid separators (' ' and '_').
    if(' ' in cc or '_' in cc):
        return False

    c = 0
    tempcc = cc.replace('-', '')
    for i in range(len(tempcc)-1):
        # Check if there are 4 or more consecutive repeated digits.
        if(tempcc[i] != tempcc[i+1]):
            c = 0
        else:
            c += 1
        if(c == 3):
            return False

    return True


    # Input the number of credit card numbers to check.
for _ in range(int(input())):
    cc = input()
    if is_valid_credit_card(cc):
        print("Valid")
    else:
        print("Invalid")
