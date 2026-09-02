'''33	Find the longest word.	S = "find the longest word"	"longest"'''
s=input("enter the string here:").split()
m=len(s[0])
a=" "
for i in s:
	if len(i)>m:
		a=i
		m=(len(i))
print("the longest word:",a)
