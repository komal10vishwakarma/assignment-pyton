from connectivity import get_connection
def search():
    con=get_connection()
    cursor=con.cursor()
    eid=int(input("enter the employee id..."))
    query="select* from employee_pdbc where eid=%s"
    cursor.execute(query,eid)
    con.close()