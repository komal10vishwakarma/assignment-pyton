'''35	Find the first palindrome word.	S = "this madam is here"	"madam"'''
s=input("enter the string here:").split()
for i in s:
	c=i[::-1]
	if i==c:
		print("The First Palindrome Is:",i)
	
		
		
		
