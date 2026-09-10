print("========================================")
print("       NUMBER ANALYSIS SYSTEM")
print("========================================")

def eo(n):
	for i in range(n):
		if n%2==0:
			return True
		else:
			return False

def fact(n):
	f=1
	for i in range(1,n+1):
		f=f*i
	print("factorial of number is:",f)
	return fact

def s(n):
	sum=0
	for i in range(0,n+1):
		sum=sum+i
	print("the value of sum is:",sum)
	return s

def nod(n):
	x=str(n)
	z=len(x)
	print("The lenght of number is:",z)
	return nod

def rev(n):
	x=str(n)
	y=x[::-1]
	print("The reverse of a number is:",y)
	return rev

def pal(n):
	x=str(n)
	r=x[::-1]
	if x==r:
		print("Number is palindrome")
	else:
		print("Number is not palindrome")
		
	return pal
	

while True:
	print("""
	1. Check Perfect Number
	2. Check Palindrome Number
	3. Check Strong Number
	4. Check Armstrong Number
	5. Check Prime Number
	6. Check Even or Odd
	7. Find Factorial
	8. Find Sum of Digits
	9. Reverse a Number
	10. Find Number of Digits
	11. Check Automorphic Number
	12. Check Neon Number
	13. Check Spy Number
	14. Check Harshad Number
	15. Exit
	""")
	choice=int(input("enter your choice here:"))	
	match choice:
		case 6:
			n=int(input("enter your number:"))
			if eo(n):
				print("Entered number is even ")
			else:
				print("Entered number is odd")
		case 7:
			n=int(input("enter your number:"))
			fact(n)
		case 8:
			n=int(input("enter your number:"))
			s(n)
		case 10:
			n=int(input("enter your number:"))
			nod(n)
		case 9:
			n=int(input("enter your number:"))
			rev(n)
		case 2:
			n=int(input("enter your number:"))
			pal(n)
			
			
			

		

			
