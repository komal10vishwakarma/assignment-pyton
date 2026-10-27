'''
48	Find the product of all elements except the current element.	[1, 2, 3, 4]	[24, 12, 8, 6]
'''
l=list(map(int,input("enter element :").split()))
for i in range(len(l)):
	x=1
	for j in l:
		if l[i]==j:
			pass
		else:
			x*=j
	l[i]=x
	x=1

print(l)
			
			
	
	
