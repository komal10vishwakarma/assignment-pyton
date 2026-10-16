'''
39	Group numbers into even and odd lists.	[1, 2, 3, 4, 5, 6]	Even: [2, 4, 6], Odd: [1, 3, 5]
'''
l1=list(map(int,input("enter the list1 element here:").split()))
even=[]
odd=[]
for i in l1:
	if i%2==0:
		even.append(i)
	else:
		odd.append(i)
print("even:",even)
print("odd:",odd)
	