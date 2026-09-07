print('''
========== EMPLOYEE DATA PROCESSING SYSTEM ==========
1. Find Second Highest Employee Age
2. Count Senior Employees
3. Remove Duplicate Ages
4. Count Names Starting with a Vowel
5. Find Longest Employee Name
6. Exit
=========================================================''')
def ages():
	age=[]
	n=int(input("enter the number is employees:"))
	for i in range(n):	
		age.append(int(input()))
	print(age)
	return age
ages()

def emp_name():
	name=[]
	n=int(input("enter the how many names you want:"))
	for i in range(n):
		name.append(input())
	print(name)
	return name


choice=int(input("Enter the choice here:"))
while True:
	match choice:
	
		case 1:
			u=ages()
			second=sorted(u,key=lambda x:x )
			print("Second Highest Age : ",second[-2])
		case 2:
			senior=ages()
			def cse():
				count=0
				for i in senior:
					if i>50:
						count=count+1
				print("Senior Employees :",count)
			cse()
			
		case 3:
			a=ages()
			s=set(a)	
			print("Unique Ages",s)	
		case 4:

			b=emp_name()
				
			vowels=('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
			result=filter(lambda x: x.startswith(vowels),b)
			print("Names Starting with Vowel :",list(result))
		case 5:
			n=emp_name()
			longest=n[0]
			for k in n:
				if len(k)>len(longest):
					longest=k
			print(longest)
				
								
		
			
		
	
		
	