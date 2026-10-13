'''
13	Find the sum of all list elements.	[10, 20, 30]	60
'''
l=list(map(int,input("enter the value:").split()))
sum=0
for i in l:
	sum=sum+i
print(sum)