'''Write a recursive program to print numbers from n to 1, where n is entered by the user.'''
n=int(input("enter the number:"))
def fun(n):
	if n==0:
		return 0
	print(n)
	fun(n-1)
fun(n)

	