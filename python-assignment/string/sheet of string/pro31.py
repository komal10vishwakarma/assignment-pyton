'''31	Remove duplicate words.	S = "the cat and the dog"	"the cat and dog'''
string=input("enter the string here:").split()
s=" "
for i in string:
	if i not in s:
		s=s+i
	elif i in s:
		continue
print(s,sep=" ")
		