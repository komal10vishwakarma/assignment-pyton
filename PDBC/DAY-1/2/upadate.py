from connectivity import get_connection
def update():
    con=get_connection()
    cursor=con.cursor()
    eid=int(input("enter the employee id..."))
    ename=input("enter emp name...")
    department=input("enter the department here...")
    salary=float(input("enter the salary"))
    city=input("enter city here..")
    query="update employee_pdbc set ename=%s,department=%s,salary=%s,city=%s where eid=%s"
    cursor.execute(query,(ename,department,salary,city,eid))
    con.commit()
    print("updation done")
    con.close()