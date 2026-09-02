'''       MATRIX OPERATIONS MANAGEMENT SYSTEM
=========================================================


A data analysis company stores numerical information in matrix form.
To help employees perform matrix-related operations efficiently,
the company wants a menu-driven application.

The application should allow the user to:

1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

The user must enter the number of rows, columns, and all matrix
elements. The program should perform the selected operation and
display the result.'''


print("1. Add Two Matrices")

print("2. Subtract Two Matrices")

print("3. Compare Two Matrices")

print("4. Exit")
n=int(input("enter your choice:"))
match n:
	case 1:
		print("1. Add Two Matrices")

		rows1=int(input("enter the size of rows"))
		cols1=int(input("enter the size of columns:"))
		matrix1=[]
		for i in range(rows1):
			rows1=[]
			for j in range(cols1):
				rows1.append(int(input()))
			matrix1.append(rows1)
		for rows1 in matrix1:
			for value in rows1 :
				print(value,end=" ")
		print()

		rows2=int(input("enter the size of rows"))
		cols2=int(input("enter the size of columns:"))
		matrix2=[]
		for i in range(rows2):
			rows2=[]
			for j in range(cols2):
				rows2.append(int(input()))
			matrix2.append(rows2)
		for row2 in matrix2:
			for value in row2 :
				print(value,end=" ")
		print()
		
		final_matrix=[]
		for i in range(len(matrix1)):
			row=[]
			for j in range(len(matrix1[i])):
				row.append(matrix1[i][j]+matrix2[i][j])
			final_matrix.append(row)
		print(final_matrix)
				
				
				
				
		
		
	case 2:
		print("2. Subtract Two Matrices")
		row1=int(input("enter the size of the row:"))
		col1=int(input("enter the side of the column:"))
		matrix1=[]
		for i in range(row1):
			row1=[]
			for j in range(col1):
				row1.append(int(input()))
			matrix1.append(row1)
		for row1 in matrix1:
			for value in row1:
				print(value,end="")
		print()

		row2=int(input("enter the size of the rows:"))
		col2=int(input("enter the size of the columns:"))
		matrix2=[]
		for i in range(row2):
			row=[]
			for j in range(col2):
				row.append(int(input()))
			matrix2.append(row)
		for row in matrix2:
			for value in row:
				print(value,end=" ")
		print()
		
		final_matrix=[]
		for i in range(len(matrix1)):
			row=[]
			for j in range(len(matrix1[i])):
				row.append(matrix1[i][j]-matrix2[i][j])
			final_matrix.append(row)
		print(final_matrix)		
		
	case 3:
		print("3. Compare Two Matrices")
		row1=int(input("enter the size of the row:"))
		col1=int(input("enter the side of the column:"))
		matrix1=[]
		for i in range(row1):
			row1=[]
			for j in range(col1):
				row1.append(int(input()))
			matrix1.append(row1)
		for row1 in matrix1:
			for value in row1:
				print(value,end="")
		print()

		row2=int(input("enter the size of the rows:"))
		col2=int(input("enter the size of the columns:"))
		matrix2=[]
		for i in range(row2):
			row=[]
			for j in range(col2):
				row.append(int(input()))
			matrix2.append(row)
		for row in matrix2:
			for value in row:
				print(value,end=" ")
		print()
		
		final_matrix=[]
		for i in range(len(matrix1)):
			row=[]
			for j in range(len(matrix1[i])):
				if (matrix1[i][j]==matrix2[i][j]):
					row.append(matrix1[i][j])
					print("matrix is equal")
				
				else:
					print("matrix in not equal")
			final_matrix.append(row)
		print(final_matrix)		

	case 4:
		print("4. Exit")
		


