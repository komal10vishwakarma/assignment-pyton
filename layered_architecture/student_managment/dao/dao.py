
from database.connectivity import Database
from model.model import Student
class Operations:
    def add(self,student):
      db=Database()
      connection=db.connect()
      cur=connection.cursor()
      query="insert into students (name,rollnum.marks) values (%s,%s,%s)"
      values=(student.name,student.rollnum,student.marks)
      cur.execute(query,values)
      connection.commit()
    print("emp saved successfully.....")

    def view(self):
       db=Database()
       connection=db.connect()
       cur=connection.cursor()
       query="select * from students "
       cur.execute(query)
       connection.close()
       row=cur.fetchall()
       for i in row:
            print(i)
       cur.close()
       connection.close()
       print("this is all the data i have right now....") 

    def update(self,student):
       db=Database()
       connection=db.connect()
       cur=connection.cursor()
       query="update students set name=%s, age=%s, marks=%s where rollnum=%s"
       values=(student.name,student.age,student.marks,student.rollnum)
       cur.execute((query,values))
       connection.commit()
       print("Student updated successfully")
       cur.close()
       connection.close()

    def delete():
       db=Database()
       connection=db.connect()
       cur=connection.cursor()
       rollnum=int(input("enter the roll number here..."))
       query="delete from student where rollnum=%s"
       cur.execute(query,(rollnum,))
       connection.commit()
       print("Student deleted successfully")
       cur.close()


       

             