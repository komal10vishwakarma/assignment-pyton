from connectivity import connect_db

# 6. UPDATE PRODUCT PRICE
# -----------------------

# INPUT
# -----
# Enter your choice: 6
# Enter Product ID: 102
# Enter New Price: 900
def updatepro():
    conn=connect_db()
    cursor=connect_db.cursor()
    price=int(input("Enter New Price:"))
    product_id=int(input("Enter Product ID:"))
    query="update product_order_pdbc set price=%s where product_id=%s "
    cursor.execute(query,(price,product_id))
    conn.commit()
    print("""OUTPUT
------
Product price updated successfully.""")
    conn.close()
