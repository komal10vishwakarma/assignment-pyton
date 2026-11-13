
from connectivity import get_connection

def delete():
    con = get_connection()
    cursor = con.cursor()

    student_id = int(input("Enter student ID you want to delete: "))

    query = "DELETE FROM students WHERE student_id = %s"

    cursor.execute(query, (student_id,))
    con.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("Student ID not found!")

    cursor.close()
    con.close()
