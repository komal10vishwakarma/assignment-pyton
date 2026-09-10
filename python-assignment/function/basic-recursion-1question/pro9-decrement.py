'''Write a recursive program to find the sum of odd numbers from 1 to n'''
n=int(input("enter the number here:"))
def so(n):
	sum=0
	if n==1:
		return 1
	elif n%2!=0:
		sum=sum+n
	return n+so(n-2)
print(so(n))
		
		
		