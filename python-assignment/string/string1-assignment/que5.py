'''
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password
'''

p=input("enter your passwprd:")
digit=0
upper=0
space=30
special=0
lenght=0

if len(p)>8 and len(p)<=15:
	if p[0].isupper():
		upper=1
	for ch in p.lower():
		if  ch>='0' and ch<='9':
			digit=digit+1
		elif ch==" ":
			space=1
		else:
			special=1
else:
	print("invalid pass")

if upper==1 and space==0 and special==1 and digit>=2:
	print("valid pass")


	
		
	