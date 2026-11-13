# ===== EMPLOYEE MANAGEMENT SYSTEM =====
# 1. Add Employee
# 2. Display All Employees
# 3. Search Employee by Name
# 4. Update Employee Salary
# 5. Delete Employee
# 6. Exit
from add import add
from display import display
from search import search
from upadate import update
from delete import delete

print("===== EMPLOYEE MANAGEMENT SYSTEM =====")
while True:
    print("""
1. Add Employee
2. Display All Employees
3. Search Employee by Name
4. Update Employee Salary
5. Delete Employee
6. Exit
    """)
    choice=int(input("enter your choice here...."))
    if choice==1:
        add()
    elif choice==2:
        display()
    elif choice==3:
        search()
    elif choice==4:
        update()
    elif choice==5:
        delete()
    elif choice==6:
        print("Exit")
    else:
        print("Invalid choice")