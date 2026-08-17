'''
Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11
'''

s=input("enter the string:")
cons=0
for ch in s.lower():
	if ch=='a' or ch== 'i' or ch=='o' or ch=='e' or ch=='u'or ch==" " :
		pass
	else:
		cons=cons+1
print(cons)