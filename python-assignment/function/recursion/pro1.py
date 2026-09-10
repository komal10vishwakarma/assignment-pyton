#n=int(input("Enter the number of months:"))
sum=0
def f(n):
	if n==0:
		return 1
	r=sum
	return r+f(n-1)
print(f(5))
	