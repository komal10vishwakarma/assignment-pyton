
from connectivity import get_connection

def delete():
    con = get_connection()
    cursor = con.cursor()

    eid = int(input("Enter employee ID you want to delete: "))

    query = "DELETE FROM employee_pdbc WHERE eid = %s"

    cursor.execute(query, (eid,))
    con.commit()

    if cursor.rowcount > 0:
        print("Employee deleted successfully!")
    else:
        print("Employee not found!")

    cursor.close()
    con.close()
