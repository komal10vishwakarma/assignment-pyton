'''=========================================
STUDENT GRADE ANALYSIS
======================

Store student marks in a dictionary.

students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}

Write a program to:

* Find the student with highest marks.
* Find the student with lowest marks.

Sample Output:
Highest Marks : Ravi 92
Lowest Marks : Aman 65
'''
print("=========================================")
print("STUDENT GRADE ANALYSIS")
print("=========================================")
students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}
h=max(students ,key=students.get)
print("Highest Marks :",h,students[h])
m=min(students ,key=students.get)
print("Lowest Marks :",m,students[m])


