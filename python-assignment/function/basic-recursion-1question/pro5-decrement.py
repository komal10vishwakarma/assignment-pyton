'''Write a recursive program to print all odd numbers from 9 to 1.'''
n=int(input("enter the number here:"))
def odd(n):
	if n==0:
		return "odd"
	elif n%2!=0:
		print("odd")
	return odd(n-1)
odd(n)
		