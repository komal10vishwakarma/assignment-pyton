from packages.armstrongnumber import *
from packages.automorphic import *
from packages.evenoddnum import *
from packages.factorial import *
from packages.harshadnum import *
from packages.neon import *
from packages.numberofdigit import *
from packages.palindrome import *
from packages.perfectnumber import *
from packages.primenumber import *
from packages.spynum import *
from packages.strongnumber import *
from packages.sumofdigits import *

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
			
			
			

		

			
