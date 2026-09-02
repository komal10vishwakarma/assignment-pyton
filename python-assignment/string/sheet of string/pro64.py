'''64	Count frequency of each vowel.	S = "programming"	o: 1, a: 1 (e, i, u: 0)'''
s=input("enter the string here:")
count=0
for i in s:
	if i in 'aeiou':
		count=count+1
		print(i,count)
	