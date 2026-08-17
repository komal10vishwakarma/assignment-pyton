'''
1.  Bank Customer Account Privacy System

A national bank is developing a secure customer portal where account
numbers should not be displayed completely on the screen. For security
reasons, the system should hide all digits except the last four digits
before showing them to users.

Conditions: - Display only the last 4 digits - Replace all previous
characters with *

Input: Enter account number: 123456789012

Output: Masked Account: ****9012'''

s=input("Enter account number:")
count=0
for i in s:
	if count <8:
                print("*",end="")
	else:
		 print(i,end="")
	count+=1
          

	
	
