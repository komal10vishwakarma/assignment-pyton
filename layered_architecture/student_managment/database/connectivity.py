import mysql.connector
class Database:
    def connect(self):
        conn=mysql.connector.connect(
            Database='layered_student',
            host='localhost',
            user='root',
            port=3306,
            password='komal',
            use_pure=True
          
        )
        return conn
    