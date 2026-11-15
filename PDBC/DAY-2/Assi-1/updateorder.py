from connectivity import connect_db

# 7. UPDATE ORDER STATUS
# ----------------------

# INPUT
# -----
# Enter your choice: 7
# Enter Order ID: 1005
# Enter New Status: Delivered

# OUTPUT
# ------
# Order status updated successfully.
def updateorder():
    conn=connect_db()
    cursor=connect_db.cursor()
    status=int(input("Enter New Status:"))
    order_id=int(input("Enter Product ID:"))
    query="update customer_order_details set price=%s where order_id=%s "
    cursor.execute(query,(status,order_id))
    conn.commit()
    print("""OUTPUT
------
order price updated successfully.""")
    conn.close()
