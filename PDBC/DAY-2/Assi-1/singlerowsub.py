from connectivity import connect_db
def single():
    conn=connect_db()
    cursor=conn.cursor()
    product_id=int(input("Enter Product ID to search:"))
    query="select * from product_order_pdbc where product_id=%s" 
    cursor.execute(query,(product_id,))
    result = cursor.fetchall()
    for row in result:
        print(row)
    conn.close()