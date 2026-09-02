'''32	Count frequency of each word.	S = "apple banana apple"	apple: 2, banana: 1'''
s=input("enter the string here:").split()
es=" "

for i in s:
	count=0
	for j in s:
		if i==j:
			count=count+1
	print(i,"occurs",count,"times")
		