from connectivity import get_connection
def display():
    con=get_connection()
    cursor=con.cursor()
    cursor.execute("select* from employee_pdbc")
    for row in cursor:
        print(row)
    con.close()