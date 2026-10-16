'''
28	Find common elements between two lists.	[1, 2, 3, 4] and [3, 4, 5, 6]	[3, 4]
'''
l1=list(map(int,input("enter the list1 element here:").split()))
l2=list(map(int,input("enter the list2 element here:").split()))
l3=[]
for i in l1:
	for j in l2:
		if i==j:
			l3.append(j)
print(l3)
