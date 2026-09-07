'''131	Check if a string is a valid email address.	S = "test@example.com"	TRUE'''
s=input("enter the email here:")

if s.isalnum or s.endswith(".com") :
	print("TRUE")
else:
	print("FALSE")
