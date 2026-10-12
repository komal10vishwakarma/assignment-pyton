'''
71	Print all substrings.	S = "abc"	"a, b, c, ab, bc, abc"
'''
s=input("enter the string here:")
i=0
while i<len(s):
	j=i
	x=s[j]
	while j<len(s):
		print(x,end=" ")
		x=x+s[j]
		j=j+1
	i=i+1
