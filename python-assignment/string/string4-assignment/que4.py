'''
4.  Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop'''

s=input("Input: Enter message:")
word=s.split()
i=0
while i<len(word):
	w=word[i]
	rev=""
	j=len(w)-1
	while j>=0:
		rev=rev+w[j]
		j=j-1
	print(rev,end=" ")
	i=i+1
