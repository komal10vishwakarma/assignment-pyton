'''
29	Find elements present in the first list but not the second.	[1, 2, 3, 4] and [3, 4, 5]	[1, 2]
'''
l1=list(map(int,input("enter the list1 element here:").split()))
l2=list(map(int,input("enter the list2 element here:").split()))
l3=[]
for i in l1:
	if i not in l2:
		l3.append(i)
print(l3)
			
		