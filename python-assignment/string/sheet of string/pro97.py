'''
97	Check if two given strings appear at the end of each other (ignoring case).	S1 = "abc", S2 = "Xabc"	TRUE
'''
s1=input("enter string 1 here:")
s2=input("enter string 2 here:").lower()
s3=s2[::-1]
l=len(s1)
s=""
for i in range(l):
	x=s3[i]
	s=s+x

for j in s1:
	if j in s3:
		print("True")
	else:
		print("False")


	
	