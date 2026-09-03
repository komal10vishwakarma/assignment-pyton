'''72	Print all substrings of length n.	S = "abc", n = 2	"ab, bc"'''
s=input("enter the string here:")
n=int(input("enter the value here:"))
for i in s:
	e=""
	for j in range(n):
		e=e+s[j]
print(e)