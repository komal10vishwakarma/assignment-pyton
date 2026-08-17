'''
1
22
3 3
4  4
55555
'''

n=int(input("enter the number:"))
i=1
while i<=n:
	print()
	j=1
	while j<=i:
		if i==3 or i==4 :
			if j==1 or i==j:
				print(i,end="")
			else:

				print(" ",end="")
			
		else:
			print(i,end="")
		j=j+1
	i=i+1
	
	