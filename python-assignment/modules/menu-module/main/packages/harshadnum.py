from .sumofdigits import s
def harshad(n):
	original=n
	add=s(n)
	print(n)
	if original % add == 0:
		print("Harshad Number")
	else:
		print(" Not Harshad Number")
	
	return harshad
