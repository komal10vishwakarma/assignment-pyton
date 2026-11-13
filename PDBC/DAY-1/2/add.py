from connectivity import get_connection
def add():
    con=get_connection()
    cursor=con.cursor()
    query="insert into employee_pdbc(eid,ename,department,salary,city) values(%s,%s,%s,%s,%s)"
    n=int(input("how many employee you want to add.."))
    data=[]
    for i in range(n):
        eid=int(input("enter the employee id..."))
        ename=input("enter the employee name here...")
        department=input("enter the department of the employee here....")
        salary=float(input("enter the salary here..."))
        city=input("enter the city of the employeee here....")
        data.append((eid,ename,department,salary,city))
    cursor.execute(query,data)
    con.commit()
    print("data inserted successfully----")
    cursor.close()
    con.close()