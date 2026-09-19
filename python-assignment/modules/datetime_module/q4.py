# 4.A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

marks1= int(input("enter the number  : "))
marks2= int(input("enter the number : "))
marks3= int(input("enter the number : "))

if marks1 and marks2 and marks3 > 100:
    print("no applicable")

total_marks = (marks1 + marks2 + marks3)/3

if total_marks>80:
    print("A")
elif total_marks>=60 and total_marks<=80:
    print("B")
elif total_marks>=50 and total_marks<60:
    print("C")
elif total_marks>=45 and total_marks<50:
    print("D")
elif total_marks>=25 and total_marks<45:
    print("E")
elif total_marks>25:
    print("F")