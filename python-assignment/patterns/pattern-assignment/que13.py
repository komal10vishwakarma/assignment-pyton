
'''
1
01
101
0101
10101

'''
n=int(input("enter the number:"))
i=1
while i<=n:
	print()
	j=1
	while j<=i:
		if (i+j)%2==0:
		 	print(1,end=" ")
		else:
			print(0,end=" ")
		j=j+1
	i=i+1