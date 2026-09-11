def automor(n):
	square=n*n
	print(square)
	st=str(square)
	i=len(str(n))

	lastnumber=st[-i:]	
	print(lastnumber)
	if n==int(lastnumber):
		print("Automorphic Number")
	else:
		print("Not an Automorphic Number")
	return automor