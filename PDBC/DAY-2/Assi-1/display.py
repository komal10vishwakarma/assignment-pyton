from connectivity import connect_db

def display():
    conn=connect_db()
    cursor=conn.cursor()
    cursor.execute("select cop.Order_ID , cop.Customer_Name ,pop.Product_Name,cod.Quantity,cod.Status ,amount = quantity * price as Amount from customer_order_pdbc as cop inner join product_order_pdbc as pop on pop.product_id=cod.product_id inner join  customer_order_details as cod on cop.customer_id=cod.customer_id")
    print(cursor.fetchall)
    conn.close()
