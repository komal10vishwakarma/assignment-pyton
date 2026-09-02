'''46	Check if a substring appears at both the start and end.	S = "abcabca", Sub="abca"	TRUE'''
string=input("enter the string here:")
sub=input("enter the sub string here:")
if string[0]==sub[0]:
	if string[:-1]==sub[:-1]:
		pass
	print("TRUE")
else:
	print("FALSE")
	
	
