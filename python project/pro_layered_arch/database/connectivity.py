import mysql.connector as a

def get_connection():
    con=a.connect(
        host='localhost',
        port=3306,
        user='root',
        database='project',
        password='komal',
        use_pure=True
        
    )