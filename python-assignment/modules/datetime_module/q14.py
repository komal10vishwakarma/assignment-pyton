# 14.Write a program to accept percantage from the user and
# display grade according to the following criteria
#   Marks	  		Grade
#   > 90       		 A
#   >80 and <=90		 B
#   >=60 and <=80		 C
#   below 60		 D


percenatge= int(input("enter the percenatge  : "))


if percenatge>90:
    print("A")
elif percenatge>80 and percenatge<=90:
    print("B")
elif percenatge>=60 and percenatge<=80:
    print("C")
elif percenatge<60:
    print("D")
