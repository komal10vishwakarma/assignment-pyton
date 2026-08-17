'''34	Find the shortest word.	S = "find the shortest word"	"the" '''
s=input("enter the string:").split()
short=len(s[0])
e=""
for i in s:
	if len(i)<short:
		e=e+i
		short=i
print(e)
			
					
			
			