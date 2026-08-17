'''15Find the last occurrence of a character.'''
s=input("enter the string:")
char=input("enter the charachter:")
count=0
index=-1
for ch in s:
	if char==ch:
		index=count
	count=count+1
print("index of the charachter is",index)

