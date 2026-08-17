'''
1
10
101
1010
10101
'''

n=int(input("enter the value:"))
i=1
while i<=n:
	j=1
	while j<=i:
		if j%2==0:
			print(0,end= " ")
		else:
			print(1,end=" ")
		j=j+1
	i=i+1
	print()