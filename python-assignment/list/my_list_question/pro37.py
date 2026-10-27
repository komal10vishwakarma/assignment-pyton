'''
37	Find the intersection of three lists.	[1, 2, 3, 4], [2, 3, 5], [0, 2, 3]	[2, 3]
'''
l1=list(map(int,input("enter l1 elements :").split()))
l2=list(map(int,input("enter l1 elements :").split()))
l3=list(map(int,input("enter l1 elements :").split()))
final=[]
for i in l1:
	if i in l2 and i in l3:
		final.append(i)
print(final)