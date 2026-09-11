def pal(n):
	x=str(n)
	r=x[::-1]
	if x==r:
		print("Number is palindrome")
	else:
		print("Number is not palindrome")
		
	return pal