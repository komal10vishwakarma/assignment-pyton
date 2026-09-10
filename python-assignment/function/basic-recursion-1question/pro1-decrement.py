'''number reverse'''

def rev(n):
	if n==0:
		return 0
	print(n)
	rev(n-1)
rev(9)