'''24	Check if all characters in a string are unique.	S1 = "abc", S2 = "abca"	S1: True, S2: False'''
string=input("enter the string here:")
s=" "
for ch in string:
	if  ch not in s:
		s=s+ch
	else:
		print("False")
		break
		
else:
	print("True")


