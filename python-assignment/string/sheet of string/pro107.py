'''107	Check if a string is a pangram (contains every letter).	S = "The quick brown fox jumps over the lazy dog"	TRUE'''
s=input("enter the string here:").lower().split()
e=""
for i in s:
	for j in i:
		if j in e:
			pass
		else:
			e=e+i

e = set(e)
if len(e)==26:
	print("TRUE")
else:
	print("FALSE")
		
