'''3.

=========================================================
         MATRIX QUALITY CHECK SYSTEM
=========================================================

Scenario

A manufacturing company records quality inspection values in
matrix form. The Quality Control team wants a menu-driven
application to analyze the inspection data and generate reports.

The application should allow the user to:

1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Armstrong Numbers Row-wise
   2. Count Palindrome Numbers Column-wise
   3. Display Average of Each Row
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Armstrong Numbers Row-wise
   -------------------------------------------
   Count and display the number of Armstrong numbers
   present in each row.

   Examples:
   153, 370, 371, 407

5. Choice 2 - Count Palindrome Numbers Column-wise
   -----------------------------------------------
   Count and display the number of palindrome numbers
   present in each column.

   Examples:
   121, 131, 444, 1221

6. Choice 3 - Display Average of Each Row
   --------------------------------------
   Calculate and display the average of each row.

7. Choice 4 - Exit
   --------------------------------------
   Display:
   "Thank You for Using Matrix Quality Check System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
153 121 10
370 22 44
407 15 131

Output:
Row 1 Armstrong Count = 1
Row 2 Armstrong Count = 1
Row 3 Armstrong Count = 1

---------------------------------------------------------

Enter your choice: 2

Output:
Column 1 Palindrome Count = 0
Column 2 Palindrome Count = 3
Column 3 Palindrome Count = 2'''



print("MENU:")
print("1. Count Armstrong Numbers Row-wise")
print("2. Count Palindrome Numbers Column-wise")
print("3. Display Average of Each Row")
print("4. Exit")
n=int(input("enter your choice here:"))
match n:
	case 1:
		row1=int(input("enter the size of the rows here:"))
		col1=int(input("enter the size of the column here:"))
		matrix=[]
		for i in range(row1):
			row=[]
			for j in range(col1):
				row.append(int(input()))
			matrix.append(row)
		for i in matrix:
			for i in row:
				pass
		print(matrix)
		
		for i in matrix:
			count=0
			k=0
			for j in row:
				temp=j
				l=(len(str(j)))
				a=j%10
				a=a**l
				k=k+a
				a=a//10
			if temp==k:
				count=count+1
			print(a)
	case 2:
		row1=int(input("enter the size of the row here:"))
		col1=int(input("enter the size of the row here:"))
		matrix=[]
		for i in range(row1):	
			row=[]
			for j in range(col1):
				row.append(int(input()))
			matrix.append(row)
		print(matrix)	
		print(" Counted Palindrome Numbers Column-wise")
		for i in matrix:
			count=0
			
			for j in i:
				temp=j
				rev=0
				while j>0:
					rev=rev*10+j%10
					j=j//10
				
				if temp==rev:
					count=count+1
			print(count)
	case 3:
		row1=int(input("enter the size of  the row here:"))
		col1=int(input("enter the size of  the row here:"))
		matrix=[]
		for i in range(row1):
			row=[]
			for j in range(col1):
				row.append(int(input()))
			matrix.append(row)
		print(matrix)
		for i in matrix:
			sum=0
			for j in i:
				sum=sum+j
			
				
				
		
							
				
				
				
				
		

		
						

