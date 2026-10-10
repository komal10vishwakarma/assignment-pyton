'''
120	Find the longest substring containing only vowels.	S = "abaeiouy"	"aeiou"
'''
string=input("enter the string here:")
s=''
for i in string:
	if i in 'aeiou':
		if i not in s:
			s=s+i
print(s)
