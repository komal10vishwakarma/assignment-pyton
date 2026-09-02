print("NUMBER ANALYSIS SYSTEM")
print("""
	MENU
1. Check Perfect Number
2. Check Prime Number
3. Find Reverse of a Number
4. Calculate Factorial
5. Display Factors of a Number
6. Exit
""")
while True:
	choice=int(input("Enter Your Choice Here:"))
	match choice:
		case 1:
			def perfectn():
				n=int(input("enter the number here:"))
				sum=0
				for i in range(1,n):
					if n%i==0:
						sum=sum+i
				if sum==n:
					print("Number IS Perfect")
				else:
					print("Not Perfect Nmber")
			perfectn()
		case 2:
			def primen():
				n=int(input("enter the number here:"))
				i=2
				while i<=n//2:
					if n%i==0:
						print("not prime number")
						break
					i=i+1
				else:
					print("prime ")
					
			primen()

		case 3:
			def rev():
				n=int(input("enter the number here:"))
				rev=0

				i=0
				while n>0:
					rev =rev*10+n%10
					n=n//10
				i=i+1
				print("reversed number is:",rev)
			rev()

		case 4:
			def fact():
				n=int(input("enter the number here:"))
				fact=1
				for i in range(1,n+1):
					fact=fact*i
				print("Factorial is:",fact)
			fact()

		case 5:
			def factors():
				n=int(input("enter the number here:"))
				i=2
				while n>0:
					if n%i==0:
						print("factor of number is:",i)
					i=i+1
			factors()
	
		case _:
			print("OUT of loop ...THANK YOU")	
