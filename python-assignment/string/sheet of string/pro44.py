'''44	Check if two strings are anagrams.	S1 = "listen", S2 = "silent"	TRUE'''
s1=input("enter the s1:")
s2=input("enter the s2:")

if len(s1)!=len(s2):
	print("FALSE")
else:
	f={ }
	f2={ }
	for ch in s1:
		f[ch]=f.get(ch,0)+1
	for ch in s2:
		f[ch]=f2.get(ch,0)+1
	if f==f2:
		print("TRUE")
	else:
		print("false")
