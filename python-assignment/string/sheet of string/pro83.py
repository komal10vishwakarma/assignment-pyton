'''
83	Create a string from a byte array.	Byte[] = {72, 101, 108} (ASCII for H, e, l)	"Hel"
'''
l=list(map(int,input("enter the number").split()))
s=""
for i in l:
	
	s=s+chr(i)
print(s)

	

