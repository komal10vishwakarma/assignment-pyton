'''
5	Check whether a key exists.	Input: D={'a':1,'b':2}, key='c'	Output: False
'''
D={'a':1,'b':2}
user=input("enter the key here:")
for user in D.keys():
	if user in D:
		print("true")
	else:
		print("false")
	