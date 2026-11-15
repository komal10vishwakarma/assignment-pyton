from connectivity import connect_db
# Enter your choice: 1
# Enter Customer_ID: 6
# Enter Customer_Name: Anjali
# Enter City: Indore
# Enter Email: anjali@gmail.com
def add():
    conn=connect_db()
    cursor=conn.cursor()
    query="insert into customer_order_pdbc(Customer_ID,Customer_Name,City,Email) values(%s,%s,%s,%s)"
    n=int(input("enter how many customer you want to add..."))
    data=[]
    for i in range(n):
        Customer_ID=int(input("Enter Customer_ID:"))
        Customer_Name=input("Enter Customer_Name:")
        City=input("Enter City:")
        Email=input("Enter Email: ")
        data.append((Customer_ID,Customer_Name,City,Email))
    cursor.executemany(query,data)
    conn.commit()
    print("multiple record insereted successfully")
    cursor.close()
    conn.close() 
    return add()
