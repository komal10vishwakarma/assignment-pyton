import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="komal",
    database="college",
    use_pure=True
)

print("Connection successful")
mycursor = mydb.cursor()

query="""create table students (id int primary key,name varchar(20),age int ,address varchar(20))"""
mycursor.execute(query)
print("table created auccessfully")