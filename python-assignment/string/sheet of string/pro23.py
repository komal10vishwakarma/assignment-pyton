'''
23	Print all characters that occur exactly twice.	S = "aabbcdee"	b', 'e'
'''
str=input("enter the string:")
s=""
for i in str:
	if i not in s:
		s=s+i
		if str.count(i)==2:
			print(i)