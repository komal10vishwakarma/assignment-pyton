'''14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000'''

course = input("Enter the course: ")
user = input("Enter the user type: ")

if course.lower() == "programming":
    if user.lower() == "student":
        fee = 5000 - (5000 * 20 / 100)
        print("Final Course Fee:", fee)
    elif user.lower() == "working professional":
        fee = 5000 - (5000 * 10 / 100)
        print("Final Course Fee:", fee)
    else:
        print("Final Course Fee: 5000")

elif course.lower() == "design":
    if user.lower() == "student":
        fee = 4000 - (4000 * 20 / 100)
        print("Final Course Fee:", fee)
    elif user.lower() == "working professional":
        fee = 4000 - (4000 * 10 / 100)
        print("Final Course Fee:", fee)
    else:
        print("Final Course Fee: 4000")

elif course.lower() == "marketing":
    if user.lower() == "student":
        fee = 3000 - (3000 * 20 / 100)
        print("Final Course Fee:", fee)
    elif user.lower() == "working professional":
        fee = 3000 - (3000 * 10 / 100)
        print("Final Course Fee:", fee)
    else:
        print("Final Course Fee: 3000")

else:
    print("Invalid course entered.")
