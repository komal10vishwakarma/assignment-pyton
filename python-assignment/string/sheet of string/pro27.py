'''27	Find the last occurrence of a word.	S = "Test this test", Word = "test"	15 (index)'''
string=input("enter the string :")
string1=string.split()
s=string1[::-1]
word=input("enter the word whose index you want:")
full=len(string1)
print(full)
index=0
for i in s:
	index=index+1
	if i==word:
		full=full-index
		
	
print("the index is :",full+1)
	
	
	
