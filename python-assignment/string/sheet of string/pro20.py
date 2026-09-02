'''20 Find the lowest frequency character. '''
s=input("enter the string :")
lowest=0
c=" "
x=" "
for i in s:
	if c not in s:
		c=c+i
		pass
	else:
		lowest=i
		lowest=lowest+1
print("lowest frequency is",i)


