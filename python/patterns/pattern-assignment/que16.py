'''
a
bc
def
ghij
klmno
'''

n=int(input("enter the value:"))
i=0
ch=97
while i<=n-1:
	j=0
	while j<=i:
		print(chr(ch),end =" ")
		ch=ch+1
		j=j+1
	print()
	i=i+1
