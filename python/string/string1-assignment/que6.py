'''
Railway Ticket PNR Analyzer

A railway department wants to verify whether a PNR number is valid.

Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits

Input:
Enter PNR: PNR123456789

Output:
Valid PNR Number'''


p=input("enter password:")
count=0
if p.startswith("PNR"):
	if len(p)==12:
			
		check=p[3:]
		for i in check:
			if i.isdigit():
				count=count+1
		if count ==len(check):
			print("valid number")
			
	else:
		print("Total length should be 12 characters")


