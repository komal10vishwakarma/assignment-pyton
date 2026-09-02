'''17Remove occurrences of a character.'''
s=input("enter the string:")
char=input("enter the charachter")
c=" "
for i in s:
	if i!=char:
		c=c+i
print("the new string is:",c)