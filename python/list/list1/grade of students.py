'''5.
 Student Grade Classification System (Python List Assignment)


A school stores student marks in a list. The system must analyze the marks and generate a *clear performance report*
by grouping students into grade categories.



Write a Python program to:

* Iterate through the list of marks
* Assign grades based on marks:

  * *>= 90 → A*
  * *>= 75 and < 90 → B*
  * *>= 50 and < 75 → C*
  * *< 50 → Fail*
* Store each category in separate lists
* Count students in each category
* Display a *final structured report (important)* 

===== STUDENT GRADE REPORT =====

A Grade Students   : [95]
B Grade Students   : [82]
C Grade Students   : [67]
Fail Students      : [45, 30]

--------------------------------
A Count   : 1
B Count   : 1
C Count   : 1
Fail Count: 2
--------------------------------

Total Students: 5'''

marks=list(map(int,input("enter the marks here:").split()))
count=0
count1 = count2 = count3 = count4 = 0
A=[]
B=[]
C=[]
F=[]
print("===== STUDENT GRADE REPORT =====")
for i in marks:
	
	if i>= 90:	
		A.append(i)
		count1=count1+1

	elif i>= 75:	
		B.append(i)	
		count2=count2 + 1
	elif i>= 50:
		C.append(i)
		count3=count3 + 1
	else:
		F.append(i)	
		count4=count4 + 1

print("A Grade Students:",A)
print("B Grade Students:",B)
print("C Grade Students:",C)
print("Fail Students:",F)
count = count1 + count2 + count3 + count4

print("--------------------------------")
print("A Count :",count1)
print("B Count :",count2)
#print("C Count :",count3)
print("Fail Count :",count4)
print("--------------------------------")
print("Total:",count)