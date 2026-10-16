'''
38	Find the longest word in a list of words.	['cat', 'elephant', 'dog', 'tiger']	elephant'''

l1=list(map(int,input("enter the element here:").split(' ')))
max=len(l1[0])
for i in l1:
	if max>len(i):
		max=len(i)