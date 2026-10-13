'''
14	Calculate the average of list elements.	[10, 20, 30]	20.0
'''

l=list(map(int,input("enter the elements here:").split()))
size=len(l)
sum=0
for i in l:
	sum=sum+i


print("Average is :",sum/size)
	