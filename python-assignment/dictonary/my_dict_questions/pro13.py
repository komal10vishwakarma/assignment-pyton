'''
3	Find the key with the maximum value.	Input: D={'a':10,'b':25,'c':15}	Output: 'b'''
D={'a':10,'b':25,'c':15}
faah=(list(D.values()))
m=max(faah)
for k,v in D.items():
	if v==m:
		print(k)
		break






