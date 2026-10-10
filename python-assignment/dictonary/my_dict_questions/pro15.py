'''
5	Merge two dictionaries.	Input: A={'a':1}, B={'b':2}	Output: {'a':1,'b':2}
'''
A={'a':1}
B={'b':2}
c={}	
d={}
for k,v in A.items():
	c=[k,v]
	
	for k,v in B.items():
		d=[k,v]
		
print(c+d)
		
	