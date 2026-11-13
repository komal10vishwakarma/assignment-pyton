import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="komal",
    database="college",
    use_pure=True
)

mycursor=mydb.cursor()
query="select * from students"
mycursor.execute(query)
result=mycursor.fetchall()
for row in result:
    print(row)