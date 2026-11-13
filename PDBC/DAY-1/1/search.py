from connectivity import get_connection
def search():
    con=get_connection()
    cursor=con.cursor()
    student_id=int(input("enter student id :"))
    query="SELECT * FROM students WHERE student_id = %s;"
    cursor.execute(query,(student_id,))
    result = cursor.fetchone()

    if result:
        print("Student Found!")
        print("Student ID:", result[0])
        print("Student Name:", result[1])
        print("Age:", result[2])
        print("Course:", result[3])
    else:
        print("Student Not Found!")

    cursor.close()
    con.close()