'''121	Check if a string contains only binary digits (0/1).	S1 = "1010", S2 = "102"	S1: True, S2: False'''
s=(input("enter the string here:"))
x=len(s)
for i in range(x-1):
	if i=="0" :
		print("true")
	elif i=="1":
		print("true")
	else:
		print("false")


