'''Write a recursive program to find the sum of numbers from 1 to n.'''
n=int(input("enter the number here:"))
sum=0
def addition(n):
	if n==1:
		return 1
	return n+addition(n-1)
print(addition(n))