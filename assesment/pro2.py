s=input("enter the string here:")
ps=" "
word=len(s)-1
for i in range(len(s)):
	if  s[:word]==s[-word:]:
		ps=s[:word]
		break
	else:
		word-=1
if len(ps)==0:
	print("no substring")
else:
	print(ps)
	
	

