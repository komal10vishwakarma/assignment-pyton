'''Write a recursive program to print "Hello" 5 times using recursion.'''
def hello(n):
	if n==0:
		return "hello"
	print("hello")
	hello(n-1)
hello(5)
