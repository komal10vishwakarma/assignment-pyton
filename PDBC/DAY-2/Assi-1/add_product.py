# INPUT
# -----
# Enter your choice: 2
# Enter Product ID: 107
# Enter Product Name: Headphones
# Enter Category: Electronics
# Enter Price: 2500
# Enter Stock: 25

from connectivity import connect_db
def add_product():
    connn=connect_db()
    cursor=connn.cursor()
    query="insert into product_order_pdbc(product_id, product_name, category, price, stock) values(%s,%s,%s,%s,%s)"
    n=int(input("enter how many product you want to add..."))
    data=[]
    for i in range(n):
        product_id=int(input("Enter Product ID:"))
        product_name=input("Enter Product Name:")
        category=input("Enter Category:")
        price=int(input("Enter Price:"))
        stock=int(input("Enter Stock: "))
        data.append((product_id, product_name, category, price, stock))
    cursor.executemany(query,data)
    connn.commit()
    print("multiple record insereted successfully")
    cursor.close()
    connn.close() 
