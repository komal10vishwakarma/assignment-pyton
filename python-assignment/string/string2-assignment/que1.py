'''
Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username'''

s=input("enter the password:")

digitandletter=0
space=0
if s[0].isalpha():
    if len(s) >= 5 and len(s) <= 12:
        for ch in s:
            if ch.isalnum():
                digitandletter = 1
            elif ch.isspace():
                space = 1
            else:
                print("you entered wrong password")
    else:
        print("Length should be between 5 and 12 characters")

if digitandletter == 1 and space == 0:
    print("valid password")
else:
    print("insvalid password")	
	
