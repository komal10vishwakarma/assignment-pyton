'''
31	Find the third largest unique element.	[10, 20, 40, 40, 30, 50]	30 '''

l1=list(map(int,input("enter elements:").split()))
x=sorted(l1)
print(x)
e=[]
for i in x:
	if i not in e:
		e.append(i)
print(e)

print(e[-3])
