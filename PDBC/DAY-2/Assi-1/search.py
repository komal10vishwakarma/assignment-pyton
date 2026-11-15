from connectivity import connect_db

def search():
    conn=connect_db()
    cursor=conn.cursor()
    name=input("Enter customer name to search:")
    query="select * from customer_order_pdbc where Customer_Name like %s"
    cursor.execute(query, ('%' + name + '%',))
    result = cursor.fetchall()

    for row in result:
        print(row)
    