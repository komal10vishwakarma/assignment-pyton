from dao.dao import add,view,update,delete
try:
    while True:
            print("""
1. Add Student
2. View Students
3. Update Student
4. Delete Student
    """)
            choice=int(input("enter your choice here"))
            if choice==1:
                add()
            elif choice==2:
                view()
            elif choice==3:
                
                rollnum=int(input("enter the roll number here"))
                name=input("enter the name here....")
                age=int(input("enter the age here/..."))
                marks=int(input("enter your marks here...."))
                update()

            elif choice==4:
                delete()
except Exception as e:
    print(e)
        
    
