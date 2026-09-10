'''Write a recursive program to find the factorial of n.'''
n=int(input("enter the number here:"))
def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)
print(fact(n))
	