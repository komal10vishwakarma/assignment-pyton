'''2. College Result Processing System


A college wants to generate grades for students automatically based on their marks in an exam. The grading criteria are as follows:

* 90 and above → Grade A
* 75 to 89 → Grade B
* 60 to 74 → Grade C
* 50 to 59 → Grade D
* Below 50 → Fail

Write a Python program to display the grade of a student.

Input:
Enter marks: 67

Output:
Grade: C'''

grades=int(input("enter your grades:"))
if grades>90:
   print("Grade A")
elif grades >75 and grades<89:
   print ("Grade B")
elif grades >60 and grades<74:
   print ("Grade C")
elif grades >50 and grades<59:
   print ("Grade D")
else:
  print("fail")