'''
29	Remove occurrences of a word.	S = "a test b test c", Word = "test", Remove All "a b c"

'''

string=input("enter the string here:").split()
word=input("enter the word that you want to remove:")
new_string=" "
for i in string:
	if i!=word:
		new_string=new_string+i
print("new string is that removes the word:",new_string)