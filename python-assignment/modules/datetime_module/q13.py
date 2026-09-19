# 13. Write a  program that keeps a number from the user and generates an integer between 1 and 7 and displays the name of the weekday.
# Test Data
# Input number: 3
# Expected Output :
# Wednesday



number = int(input("Enter number: "))

if number == 1:
    print("MONDAY")
elif number == 2:
    print("TUESDAY")
elif number == 3:
    print("WEDNESDAY")
elif number == 4:
    print("THURSDAY")
elif number == 5:
    print("FRIDAY")
elif number == 6:
    print("SATURDAY")
elif number == 7:
    print("SUNDAY")