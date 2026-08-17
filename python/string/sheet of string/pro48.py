'''48	Remove all vowels.	S = "aeiou XYZ"	" XYZ" '''
string=input("enter the srting here:")
c=" "
for i in string:
	if i=='a' or i=='u' or i=='o'or i=='i'or i=='e':
		pass
	else:
		c=c+i
print(c)
