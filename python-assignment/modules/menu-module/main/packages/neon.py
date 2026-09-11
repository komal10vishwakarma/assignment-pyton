def neon(n):	
	original=n
	square=n*n
	inq=str(square)
	sum=0
	for i in inq:
		sum=sum+int(i)
	print(sum)
	if original==sum:
		print("Neon Number")
	else:
		print("Not Neon Number")
	return neon 