'''
46	Find the duplicate number in a list containing values 1 to n.	[1, 3, 4, 2, 2]	2
'''
l=list(map(int,input("enter element:").split()))
e=[]
for i in l:
	if i not in e:
		e.append(i)
	else:
		print(i)

