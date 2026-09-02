'''37	Reverse each word.	S = "cat dog"	"tac god"'''
s=input("enter the string here:").split()
c=" "
rev=0
for i in s:
	for j in i:
		rev=rev+j
		print(rev)
		