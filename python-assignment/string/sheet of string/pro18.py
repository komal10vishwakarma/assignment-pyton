'''18Replace occurrences of a character.'''
s=input("enter the string:")
word=input("enter the charachter you want to replace:")
replace=input("enter the replacing wrd:")
c=" "
for i in s:
	if i==word:
		c=c+replace
	else:
		c=c+i
		
		
print(c,end="")
		
		
		
		