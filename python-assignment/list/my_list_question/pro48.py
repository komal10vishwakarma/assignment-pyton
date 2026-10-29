'''
48	Find the product of all elements except the current element.	[1, 2, 3, 4]	[24, 12, 8, 6]
'''
l=list(map(int,input("enter element :").split()))
s=[]
i=0
while i<len(l):
	pro=1
	j=0
	while j<len(l):
		if i!=j :
			pro=pro*l[j]
		j=j+1
	s.append(pro)
	i=i+1
print(s)

			
			
			
	
	
