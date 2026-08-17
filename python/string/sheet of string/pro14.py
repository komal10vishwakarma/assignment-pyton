'''14Find the first occurrence of a character.'''
s=input("enter the sting:")
ch=input("enter the character:")
index=-1
for i in s:
	index=index+1
	if i==(ch):
		print(ch)
		break
print("INDEX IS:",index)
	
	
	
