'''
Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code'''

word=input("Enter product code:")
s=word[::-1]
if word==s:
	print("Palindrome Code")
else:
	print("Not a Palindrome Code")

 