'''68	Count the sum of digits present in a string.	S = "a1b2c3"	6 (1+2+3)'''
string=input("enter the string here")
c=" "
sum=0
for i in string:
	for j in i:
		if j.isdigit():
			sum=sum+int(j)
		else:
			pass
print("sum is ",sum)
