import mysql.connector
class Database:
    def connect(self):
        print("databse connetion created")
        connection=mysql.connector.connect(host='localhost',user='root',password='komal',database='batch 19', )

        return connection