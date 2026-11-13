from connectivity import get_connection
def update():
    con=get_connection()
    cursor=con.cursor()
    student_id = int(input("enter student id:"))
    student_name = input("enter the student name:")
    age = int(input("enter the age:"))
    course = input("enter the course:")
    query="update students set student_name=%s,age=%s,course =%s where student_id=%s"
    cursor.execute(query,(student_name,age,course,student_id))
    con.commit()
    print("updation done")
    con.close()