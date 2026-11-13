from connectivity import get_connection
def display():
    con=get_connection()
    cursor=con.cursor()
    no=int(input("how many records you want to see:"))
    cursor.execute("select*from students")
    print(cursor.fetchmany(no))
    print("done")
    con.close()
    cursor.close()
    



