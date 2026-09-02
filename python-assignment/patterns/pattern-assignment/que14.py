'''
1
23
456
78910

'''
n=int(input("enter the value:"))
i=1
k=1
while i<=n+1:
	j=1
	while j<=i:
		print(k,end=" ")
		k=k+1
		j=j+1
	print()
        i=i+1