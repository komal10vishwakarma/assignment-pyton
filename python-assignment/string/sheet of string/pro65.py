'''
65	Count palindromic substrings.	S = "aaa"	6 (a, a, a, aa, aa, aaa)
'''
s=input("enter the string here:")
i=0
while i<len(s):
	j=i
	p=s[j]
	while j<len(s):
		print(p,end=" ")
		p+=s[j]
		j=j+1
	i=i+1