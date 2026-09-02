print("******** STUDENT RESULT MANAGEMENT ********")
print("1. Add Student Details")
print("2. Calculate Total Marks")
print("3. Calculate Percentage")
print("4. Find Grade")
print("5. Display Result")
print("6. Find Highest Mark")
print("7. Find Lowest Mark")
print("8. Exit")

while True:
	n=int(input("enter your choice here:"))
	match n:
		case 1:
			name=input("Enter Student Name :")
			rollno=int(input("Enter Roll Number :"))
			number=int(input("enter the number of subject:"))
			def marks():
				m=[]
				for i in range(number):
					m.append (int(input("Enter Marks:")))
				print(m)
			marks()
			print("Student details added successfully.")
			
				
		case 2:	
			number=int(input("enter the number of subject:"))
			def marks():
				m=[]
				for i in range(number):
					m.append (int(input("Enter Marks:")))
				print(m)
				for num in m:
					c=(sum(m))
				print("Total Marks:",c)
			marks()
				
			
			
		case 3:
			number=int(input("enter the number of subject:"))
			def marks():
				m=[]
				for i in range(number):
					m.append (int(input("Enter Marks:")))
				print(m)
				for num in m:
					c=(sum(m))
				print("Total Marks:",c/500*100)
			marks()

		case 4:
			number=int(input("enter the number of subject:"))
			def marks():
				m=[]
				for i in range(number):
					m.append (int(input("Enter Marks:")))
				print(m)
				for num in m:
					c=(sum(m))
					p=c/500*100
				print("Total Marks:",p)
				if  p>80:
					print("grade A")
				elif p>50:
					print("grade B")
				else:
					print("C")
			marks()
		case 5:
			print("----------- RESULT CARD -----------")
			
		case 6:
			number=int(input("enter the number of subject:"))
			def marks():
				m=[]
				for i in range(number):
					m.append (int(input("Enter Marks:")))
				print(m)
				print("Highest Mark",max(m))
			marks()
		case 7:
			number=int(input("enter the number of subject:"))
			def marks():
				m=[]
				for i in range(number):
					m.append (int(input("Enter Marks:")))
				print(m)
				print("Lowest Mark",min(m))
			marks()
		case _:	
			print("Exit")
		