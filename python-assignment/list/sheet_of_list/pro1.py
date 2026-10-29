l=list(map(int,input("enter the elemets:").split()))
target=int(input("enter the target number here:"))
for i in range(len(l)):
	for j in range(len(l)):
		if target==l[i]+l[j]and i!=j:
			print(i,j)
			break
			
			