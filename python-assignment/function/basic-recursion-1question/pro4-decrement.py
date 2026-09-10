'''Write a recursive program to print all even numbers from 10 to 2.'''
n=int(input("enter the number here:"))
def rec(n):
	if n==1:
		return 1
	elif n%2==0:
		print("even")
	return rec(n-1)
rec(n)

		
	