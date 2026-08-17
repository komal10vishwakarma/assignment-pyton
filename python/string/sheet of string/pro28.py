'''
28	Count occurrences of a word.	S = "word word other word", Word ="word"	3
'''

string=input("enter the string here:").split()
word=input("enter the word you are looking for:")
count=0
for i in string:
	if i==word:
		count=count+1
print(count)
