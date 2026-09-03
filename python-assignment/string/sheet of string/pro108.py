'''108	Check if a string is an isogram (no repeating letters).	S = "ambidextrous"	TRUE'''
string=input("enter the string :")
e=""
for i in string:
	if i not in e:
		e=e+i
if len(string)==len(e):
	print("TRUE")
else:
	print("FALSE")

	
