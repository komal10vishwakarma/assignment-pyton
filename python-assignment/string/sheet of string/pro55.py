'''55	Reverse only vowels.	S = "hello" holle '''
s=input("enter the string here:")
e=" "
for i in s:
	if i in 'aeiou':
		e=e+i
print(e)
e=e[::-1]
print(e)
