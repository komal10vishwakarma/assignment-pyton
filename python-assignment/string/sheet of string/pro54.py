'''54	Replace duplicate chars with '$'.	'''

s=input("enter the string here:")
e=" "
for i in s:
	if i not in e:
		e=e+i
	else:
		e=e+"$"
print(e)
