'''
30	Move all zeros to the end of a list.	[0, 1, 0, 3, 12]	[1, 3, 12, 0, 0]
'''
l1=list(map(int,input("enter the list1 element here:").split()))
l2=[]
l3=[]
for i in l1:
	if i!=0:
		l2.append(i)
	else:
		l3.append(i)	
print(l2+l3)	