n=int(input("enter the number here:"))
f=n
def prime(n):
	if f%n==0:
		return "not prime"
	elif n==2:
		return "prime"
	return (prime(n-1))
if n==2:
	print("prime")
else:

	print(prime(n-1))