'''20	Find the lowest frequency character.	S = "aabbcde"	'c', 'd', 'e' (any one or all)'''
s=input("enter the string here:")
c=" "
for i in s:
	if c not in i:
		c=c+i
		print(c)
	else:
		print(c)
		
		


