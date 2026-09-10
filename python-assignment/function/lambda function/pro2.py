e=int(input("Enter the number of employees:"))

salary=[]
for i in range(e):
	salary.append(int(input()))
print("Enter the salaries:",*salary)

result=filter(lambda x: x>50000 ,salary)


print("sample output")
print("Eligible Employees' Updated Salaries:")
final=map(lambda x:x+x*0.10,result)
print(list(final))
