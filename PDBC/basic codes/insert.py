import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="komal",
    database="college",
    use_pure=True
)

mycursor=mydb.cursor()
query="""
insert into students (id,name,age,address) values (1,'komal',21,'indore'),(2,'shreeji',23,'indore'),(3,'deep',31,'chennai'),(4,'deep',32,'delhi'),(5,'reep',33,'gujrat')"""
mycursor.execute(query)

#commit() permanently saves the changes made by your transaction
mydb.commit()
print("Records inserted successfully")