'''
22	Create a list containing squares of numbers from 1 to 5.	[1, 2, 3, 4, 5]	[1, 4, 9, 16, 25]
'''
l1=list(map(int,input("enter the list element:").split()))
l2=[]
for i in l1:
	i=i*i
	l2.append(i)
print(l2)