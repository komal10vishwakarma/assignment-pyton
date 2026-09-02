'''
Create a function to check whether a person is eligible to vote.
'''
def eligible( ):
	age=int(input("enter the age here:"))
	if age>18:
		print("eligible to vote")
	else:
		print("not eligible")
eligible()
	