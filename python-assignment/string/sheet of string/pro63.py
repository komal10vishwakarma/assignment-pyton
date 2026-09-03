'''63	Count frequency of each character.	S = "aabcc"	a: 2, b: 1, c: 2'''
string=input("enter the string here:")
e=""
for i in string:
	
	if i not in e:
		e=e+i
		print(i,":",string.count(i))
	else:
		e=e+i
