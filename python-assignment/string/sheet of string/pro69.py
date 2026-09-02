'''69	Count how many times 'life' appears in a string.	S = "life is life"	2'''
s=input("enter the string here:").split()
word=input("enter the word that you want to find out:")
count=0
for i in s:
	if i==word:
		count+=1
print(count)
