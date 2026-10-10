'''
1	Create a dictionary with three key-value pairs.	Input: name='Asha', age=20, city='Delhi'	Output: {'name':'Asha','age':20,
'city':'Delhi'}

'''
d={}
n=int(input("enter the number:"))
for i in range(n):
	name=input("enter the name")
	age=int(input("enter the age:"))
	city=input("enter the city :")
	d['name']=name
	d['age']=age
	d['city']=city
print(d)
for k,v in d.items():
	print(k,v)