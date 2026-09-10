'''Write a recursive program to find the sum of even numbers from 2 to n.'''
n=int(input("enter the number here:"))

def se(n):
	sum=0
	if n==2:
		return 2
	elif n%2==0:
		sum=sum+n
	return n+se(n-2)
	se(n-1)
print(se(n))