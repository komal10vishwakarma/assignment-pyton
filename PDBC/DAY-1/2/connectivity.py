import mysql.connector

def get_connection():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="komal",
        database="pdbc_EMPLOYEE_MANAGEMENT_SYSTEM",
        use_pure=True
    )
    return con