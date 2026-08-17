'''50	Remove all digits.	S = "a1b2c3"	"abc" '''
string=input("enter the string here:").split()
c=" "
for i in string:
	for j in i:
		if j.isalpha():
			c=c+j
		else:
			print("string not contain any digit")
print(c,end= " ")
			
