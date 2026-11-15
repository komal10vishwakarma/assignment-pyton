import mysql.connector

def connect_db():
    con = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='komal',
        database='day2_pdbc_online_shopping_order_management_system',
        use_pure=True
    )
    return con

