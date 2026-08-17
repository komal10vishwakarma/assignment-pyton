'''53	Remove punctuation.	S = "Hello, world!"	"Hello world"'''
string=input("enter the input:")
c=" "
for i in string:
	if i.isalpha():
		c=c+i
print(c)
