'''16Count total occurrences of a character.'''
s=input("enter the string:")
char=input("enter the charachter:")
count=0
for i in s:
	if i==char:
		count=count+1
print(count)