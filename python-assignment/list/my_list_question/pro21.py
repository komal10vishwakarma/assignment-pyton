'''
21	Remove duplicate elements from a list while preserving order.	[1, 2, 2, 3, 1, 4]	[1, 2, 3, 4]
'''
l1=list(map(int,input("enter the list element:").split()))
l2=[]
for i in l1:
	if i not in l2:
		l2.append(i)
print(l2)
