'''
23	Create a list of even numbers from a given list.	[1, 2, 3, 4, 5, 6]	[2, 4, 6]
24	Create a list of odd numbers from a given list.	[1, 2, 3, 4, 5, 6]	[1, 3, 5]
'''

l1=list(map(int,input("enter the list element:").split()))
l2=list(map(int,input("enter the list element:").split()))
l3=[]
l4=[]
for i in l1:
	if i%2==0:
		l3.append(i)
print(l3)

for j in l2:
	if j%2!=0:
		l4.append(j)
print(l4)
	
	