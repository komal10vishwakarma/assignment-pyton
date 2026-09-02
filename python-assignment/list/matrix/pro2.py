'''=======================================================
            MATRIX ANALYSIS SYSTEM
=========================================================


A research laboratory stores experimental data in matrix form.
Scientists want a program that can analyze the matrix and provide
different statistics through a menu-driven application.

The application should allow the user to:

1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit'''
 
print("1. Count Prime Numbers Row-wise")
print("2. Count Perfect Numbers Column-wise")
print("3. Display Row-wise Sum")
print("4. Exit")
n=int(input ("choose and otption here:"))
match n:
	case 1:
		print("1. Count Prime Numbers Row-wise")
		row1=int(input("enter the size of row in matrix1= "))
		col1=int(input("enter the size of col in matrix1= "))
		matrix1=[]
		for i in range(row1):
			row=[]
			for j in range(col1):
				row.append(int(input()))
			matrix1.append(row)
		for value in matrix1:
			for value in row:
				pass
		print(matrix1)
		matrix2=[]
		
		for i in matrix1:
			count=0
			for j in i:
				for x in range(2,j//2):
					if j%x==0:		
					 	break
					
				else:
					count+=1
			else:
				matrix2.append(count)

		print(matrix2)
			
			

	case 2:
		print("2. Count Perfect Numbers Column-wise")
		row1=int(input("enter the size of row in matrix1= "))
		col1=int(input("enter the size of col in matrix1= "))
		matrix1=[]
		for i in range(row1):
			row=[]
			for j in range(col1):
				row.append(int(input()))
			matrix1.append(row)
		for value in matrix1:
			for value in row:
				pass
		print(matrix1)
		
		for i in matrix1:
			l=[]
			sum=0
			for j in i:
				for x in range(1,j//2):
					if j%x==0:
						l.append(x)
						sum=sum+x
			print(sum)
					
				


	case 3:
		print("3. Display Row-wise Sum")
		row1=int(input("enter the size of row in matrix1= "))
		col1=int(input("enter the size of col in matrix1= "))
		matrix1=[]
		for i in range(row1):
			row=[]
			for j in range(col1):
				row.append(int(input()))
			matrix1.append(row)
		for value in matrix1:
			for value in row:
				pass
		print(matrix1)
		for i in matrix1:
			sum=0
			for j in i:	
				sum=sum+j
			print(sum)
	case 4:
		print("you are exists")
				