'''
16	Sort a list in ascending order.	[5, 1, 4, 2, 3]	[1, 2, 3, 4, 5]
17	Sort a list in descending order.	[5, 1, 4, 2, 3]	[5, 4, 3, 2, 1]
'''

l1=list(map(int,input("enter the elements of list 1 here:").split()))
l2=list(map(int,input("enter the elements of list 2 here:").split()))
l1.sort()
print("ascending order.",l1)
l2.sort(reverse=True)
print("descending order.",l2)


