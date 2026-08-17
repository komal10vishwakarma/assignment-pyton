'''49	Replace all consonants with '*' (Example suggests replacing non-vowels). S = "apple"   "ap*le" (or similar output depending on implementation)'''

string=input("Enter the string here:").split()
c=" "
for i in string:
	for j in i:
		if j=='a' or j=='u' or j=='o' or j=='i' or j=='e' :
			c=c+j
		else:
			j=="*"
			c=c+"*"		
print(c,end=" ")

		
		
