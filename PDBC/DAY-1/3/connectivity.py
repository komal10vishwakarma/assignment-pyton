
import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="komal",
        database="PRODUCT_INVENTORY_SYSTEM",
        use_pure=True
    )

    return conn
