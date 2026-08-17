n=list(map(int,input("enter the list items:").split()))
for i in n: 
	rev=0
	while i>0:
		rev=rev*10+i%10
		i=i//10
        print(rev)