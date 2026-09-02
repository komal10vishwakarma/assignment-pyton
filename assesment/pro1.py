r1=int(input("enter the number of rows"))
c1=int(input("enter the number of column"))
print("enter the elements here:")
a=[]
for i in range(r1):
	row=[]
	for j in range(c1):
		row.append(int(input( )))
	a.append(row)
print (list(a))

print("Main Diagonal Elements:")	
for i in range(r1):
	for j in range(c1):
		if  i==j:
			print (a[i][j],end=" ")

print("Secondary Diagonal Elements:")
for i in range(r1):
	for j in range(c1,-1,-1):
		if  i==j:
			print (a[i][j],end=" ")


