'''
33	Rotate a list to the left by 2 positions.	[1, 2, 3, 4, 5]	[3, 4, 5, 1, 2]
'''
l=list(map(int,input("enter elements:").split()))
x=l[:2]

y=l[2:]

print(y+x)
	