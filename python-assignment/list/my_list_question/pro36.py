'''
36	Merge two sorted lists into one sorted list.	[1, 3, 5] and [2, 4, 6]	[1, 2, 3, 4, 5, 6]
'''
l1=list(map(int,input("enter the list1 element here:").split()))
l2=list(map(int,input("enter the list2 element here:").split()))
l3=l1+l2
l3.sort()
print(l3)