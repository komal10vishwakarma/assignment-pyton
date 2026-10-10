'''
4	Find the key with the minimum value.	Input: D={'a':10,'b':25,'c':15}	Output: 'a'
'''
D={'a':10,'b':25,'c':15}
l=(list(D.values()))
x=min(l)
for k,v in D.items():
	
	if v==x:
		print(k)
		break

