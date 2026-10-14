'''
25	Separate positive and negative numbers.	[-3, 5, -1, 8, -2, 4]	Positive: [5, 8, 4], Negative: [-3, -1,
-2]

'''

l1=list(map(int,input("enter the list element:").split()))
positive=[]
negative=[]
for i in l1:
	if i<=0:
		negative.append(i)
	else:
		positive.append(i)
print(positive)
print(negative)
