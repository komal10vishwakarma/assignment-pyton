'''
27	Reverse a list without using reverse().	[1, 2, 3, 4]	[4, 3, 2, 1]
'''
l1=list(map(int,input("enter the list element:").split()))
l2=[]
lenth=len(l1)
for i in range(lenth-1,-1,-1):
	l2.append(l1[i])
print(l2)

	
	
