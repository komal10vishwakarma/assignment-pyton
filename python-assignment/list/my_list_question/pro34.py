'''
34	Find all pairs whose sum equals a target.	[2, 4, 3, 5, 7], target 7	[(2, 5), (4, 3)]
'''
l=list(map(int,input("enter the list elements:").split()))
n=int(input("enter the element target number"))
x=len(l)
l1=[]
i=0
while i<x:
	j=0
	while j<x:
		if l[i]+l[j]==n and (l[j],l[i]) not in l1:
			l1.append((l[i],l[j]))
		j=j+1
	i=i+1
print(l1)
		
			

