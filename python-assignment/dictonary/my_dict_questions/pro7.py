'''
7	Find the number of key-value pairs.	Input: D={'a':1,'b':2,'c':3}	Output: 3'''
D={'a':1,'b':2,'c':3}
count=0
for k,v in D.items():
	count=count+1
print(count)