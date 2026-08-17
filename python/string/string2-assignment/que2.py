'''
Mobile Number Digit Counter

A telecom company wants to count how many digits are present in a customer contact number entered with spaces or symbols.

Input:
Enter contact number: +91 98765-43210

Output:
Total digits: 12'''

s=input("enter the number")
digit=0
for ch in s[0:]:
	
	if ch.isdigit():
		digit =digit+1
	
	
print(digit)


