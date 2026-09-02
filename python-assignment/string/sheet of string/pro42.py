'''42	Check if two strings are equal without equals().	S1 = "abc", S2 = "abc"	TRUE'''
s1=input("enter the string 1 here:").split()
s2=input("enter the string 2 here:").split()
if len(s1)==len(s2):
	for ch in s1:
		for i in s2:
			if ch==i:
				print("TRUE")
			else:
				print("FALSE")


				

