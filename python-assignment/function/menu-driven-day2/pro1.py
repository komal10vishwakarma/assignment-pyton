


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
	num=str(n)
	sum=0
	for i in num:
		sum=sum+int(i)
	print("the value of sum is:",sum)
	return sum

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

	
def spy(n):
	add=s(n)
	print(add)
	num=str(n)
	pro=1
	for i in num:
		pro=pro*int(i)
	print(pro)
	if add==pro:
		print("Spy Number")
	else:
		print("Not Spy Number")
	return spy	
	
		
def harshad(n):
	original=n
	add=s(n)
	print(n)
	if original % add == 0:
		print("Harshad Number")
	else:
		print(" Not Harshad Number")
	
	return harshad

def perfect_number(n):
	sum = 0
	for i in range(1, n):
		if n % i == 0:
			sum = sum + i
	if sum == n:
			print(n, "is a Perfect Number")
	else:
			print(n, "is not a Perfect Number")

	

	
def prime(n):
	if n%2==0:
		print("Prime Number")
	else:
		print("Not Prime Number")
	



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
		case 1:
			n = int(input("Enter a number: "))
			perfect_number(n)
		case 2:
			n=int(input("enter your number:"))
			pal(n)

		case 3:
			pass
		case 4:
			n = int(input("Enter a number: "))
			prime(n)
		case 5:
			n=int(input("enter your number:"))
			prime(n)
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
		case 9:
			n=int(input("enter your number:"))
			rev(n)
		case 10:
			n=int(input("enter your number:"))
			nod(n)
		case 11:
			n=int(input("enter your number:"))
			automor(n)
		case 12:
			n=int(input("enter your number:"))
			neon(n)
		case 13:
			n=int(input("enter your number:"))
			spy(n)
		case 14:
			n=int(input("enter your number:"))
			harshad(n)
		case 15:
			print("exit")
		
		case _:
			print("You are out of loop")
			
			
			

		

			
