'''
6	Delete a key from a dictionary.	Input: D={'a':1,'b':2}, delete='a'	Output: {'b':2}
'''
D={'a':1,'b':2}
delete=input("enter the key here:")

if delete in D:
	D.pop(delete)
	print(D)
else:
	print("key no exists")


		 

