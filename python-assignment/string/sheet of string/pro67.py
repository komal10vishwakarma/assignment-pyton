'''
67	Count how many times a substring appears.	S = "abab", Sub = "ab"	2
'''
s=input("enter the string here:")
sub=input("enter the sub string here:")
l=len(sub)
count=0
for i in range(len(s)):
	if sub in s:
		count=count+1
print(count)
