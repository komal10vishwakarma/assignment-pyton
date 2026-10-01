students = {}


def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")

    python = int(input("Enter Python Marks: "))
    maths = int(input("Enter Maths Marks: "))
    english = int(input("Enter English Marks: "))
    computer = int(input("Enter Computer Marks: "))

    students[roll_no] = {
        "name": name,
        "python": python,
        "maths": maths,
        "english": english,
        "computer": computer
    }

    print("Student added successfully!")


def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def display_student():

    roll_no = input("Enter Roll Number: ")

    if roll_no in students:

        student = students[roll_no]

        total = (
            student["python"]
            + student["maths"]
            + student["english"]
            + student["computer"]
        )

        percentage = total / 4

        grade = calculate_grade(percentage)

        print("\n----- Student Details -----")
        print("Roll Number:", roll_no)
        print("Name:", student["name"])
        print("Python:", student["python"])
        print("Maths:", student["maths"])
        print("English:", student["english"])
        print("Computer:", student["computer"])
        print("Total Marks:", total)
        print("Percentage:", percentage)
        print("Grade:", grade)

    else:
        print("Student not found!")


def display_all_students():

    if len(students) == 0:
        print("No students available.")
        return

    print("All Students")

    for roll_no, student in students.items():

        total = (
            student["python"]
            + student["maths"]
            + student["english"]
            + student["computer"]
        )

        percentage = total / 4
        grade = calculate_grade(percentage)

        print("\nRoll Number:", roll_no)
        print("Name:", student["name"])
        print("Total:", total)
        print("Percentage:", percentage)
        print("Grade:", grade)


def student_applicataion():
    while True:

        print("STUDENT GRADE MANAGER")
        print("1. Add Student")
        print("2. Display Student")
        print("3. Display All Students")
        print("4. Exit")
    
        choice = input("Enter your choice: ")
    
        if choice == "1":
            add_student()
    
        elif choice == "2":
            display_student()
    
        elif choice == "3":
            display_all_students()
    
        elif choice == "4":
            print("Thank you for using Student Grade Manager!")
            break
        else:
            print("Invalid choice!") 