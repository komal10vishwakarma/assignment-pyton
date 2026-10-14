'''
15	Check whether a value exists in a list.	[3, 7, 9, 12], search 9	True
'''
l=list(map(int, input("enter the list element:").split()))
word=int(input("enter the searching element here:"))
if word in l:
	print("True")
else:
	print("False")