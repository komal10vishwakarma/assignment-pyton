# 7. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.





classes_held= int(input("enter classes held : "))
classes_attend= int(input("enter classes attend : "))

percentage = (classes_attend/classes_held)*100

if percentage>=75:
    print(f"classes attend : {percentage} %")
    print(f"you are eligible to attend exam")
else:
    print(f"classes attend : {percentage} %")
    print(f"you are not eligible to attend exam")

