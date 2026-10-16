'''
32	Rotate a list to the right by 2 positions.	[1, 2, 3, 4, 5]	[4, 5, 1, 2, 3]
'''
l1=list(map(int,input("enter the element here:").split()))
x=l1[-2:]
y=l1[:-2]
print(x+y)
