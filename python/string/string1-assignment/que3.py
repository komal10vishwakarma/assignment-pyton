'''

Character Occurrence Checker in Product Review

An e-commerce website wants to know how many times a particular character appears in a product review.

Input: Enter product review: this product is really good Enter character to check: o

Output: Character 'o' occurs: 4 times
'''
s=input("enter the string:")
t=input("enter the charchter you want to check:")
repeat=0
for ch in s.lower():

	if ch==t:
		repeat=repeat+1
print(repeat)