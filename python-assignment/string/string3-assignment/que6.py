'''
The company wants a Python program to count how many times a particular word appears in a review.

Input Sentence:


iphone is good and iphone battery is strong


Word:
iphone


Output:
2
---'''
'''
s=input("Input Sentence:")
words = s.split()
count=0
visited=""
for word in words:
	
	if word in visited:
		count=0
		for w in words:
			if word==visited:
	
				count=count+1
print(count)'''

s=input("enter the string")
w=s.split()
for i in range (0,len(w)):
	b=w[i]
	rev=""
	for j in range (0,len(b)):
		rev=b[j]+rev
	print (rev,end=" ")
























		