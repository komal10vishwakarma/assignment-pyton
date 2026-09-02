'''
Create a function to check whether a number is positive, negative, or zero.
'''
def pnz():
	n=int(input("enter the number here:"))
	if n==0:
		print("Zero")
	elif n>0:
		print("Positive")
	else:
		print("negative")
pnz()