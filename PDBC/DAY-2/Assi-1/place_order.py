from connectivity import connect_db

# Enter your choice: 3
# Enter Order ID: 1008
# Enter Customer ID: 6
# Enter Product ID: 107
# Enter Quantity: 2
# Enter Order Status: Pending
def place_order():
    conn=connect_db()
    cursor=conn.cursor()
    query=" insert into customer_order_details(order_id, customer_id, product_id, quantity, order_status) values (%s,%s,%s,%s,%s)"
    n=int(input("enter how many order you have to you..."))
    data=[]
    for i in range(n):
        order_id=input("Enter Order ID:")
        customer_id=int(input("Enter Customer ID:"))
        product_id=int(input("Enter Product ID:"))
        quantity=int(input("Enter Quantity:"))
        order_status=input("Enter Order Status:")
        data.append((order_id, customer_id, product_id, quantity, order_status))
    cursor.executemany(query,data)
    conn.commit()
    print("succesfully multiple order placed")
    cursor.close()
    conn.close
    return place_order