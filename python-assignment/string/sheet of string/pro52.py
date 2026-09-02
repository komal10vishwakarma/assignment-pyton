'''52	Remove all special characters.	S = "a!@b#c"	"abc" '''
string=input("enter the string here:")
c=" "
for i in string:
	if i.isalnum():
		c=c+i
print(c)
	
	
