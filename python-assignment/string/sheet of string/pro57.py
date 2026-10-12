'''57	Merge two strings alternatively.	S1 = "ABC", S2 = "def" AdBeCf '''
s1=input("enter the string 1 here:")
s2=input("enter the string 2 here:")
s3=""
lenght1=len(s1)
lenght2=len(s2)	
o=lenght1+lenght2
i=0
j=0
k=0
while k<o:
	if k%2 == 0:
		s3+=s1[i]
		i+=1
	else:
		s3+=s2[j]
		j+=1
	k+=1
print(s3)
		

	
		
	
