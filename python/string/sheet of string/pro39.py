'''39	Search all occurrences of a character.	S = "banana", Char='a'	1, 3, 5 (indices)'''
s=input("enter the string here:")
char=input("enter the character here:")
index=-1
c=" "
for i in s:
	if i!=char:
		c=c+i
		index=index+1
	else:
		index=index+1
		print(index)
		

	