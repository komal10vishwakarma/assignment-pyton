'''
19	Join two lists.	[1, 2, 3] and [4, 5, 6]	[1, 2, 3, 4, 5, 6]
'''
l1=list(map(int,input("enter the elements here:").split()))
l2=list(map(int,input("enter the elements here:").split()))


s=l1+l2
print(s)