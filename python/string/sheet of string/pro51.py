'''51	Extract only digits.	S = "a1b2c3"	"123" '''
s=input("enter the string:").split()
c=""
for i in s:
	for j in i:
		if j.isdigit():
			c=c+j
print(c)
