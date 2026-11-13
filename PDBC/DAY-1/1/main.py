from add import add
from display import display
from search import search
from display import display
from delete import delete

print("===== STUDENT MANAGEMENT SYSTEM =====")

while True:
    print("""
1. Add Student
2. Display All Students
3. Search Student by Name
4. Update Student Fees
5. Delete Student
6. Exit
    """ )
    choice=int(input("enter your choice here..."))
    if choice==1:
        print("Add Student")
        add()
    elif choice==2:
        print("Display All Students")
        display()
    elif choice==3:
        print("Search Student by Name")
        search()
    elif choice==4:
        print(" Update Student Fees")
        display()
    elif choice==5:
        print("Delete Student")
        delete()
    elif choice==6:
        print("EXIT")
        break

    else:
        print("Invalid choice")

    