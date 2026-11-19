
from database.connectivity import Database
from model.model import Student
class Operations:
    def add(self):
      db=Database()
      connection=db.connect()
      cur=connection.cursor()
      query="insert into students (name,rollnum.marks) values (%s,%s,%s)"
      values=(Student.name,Student.rollnum,Student.marks)
      cur.execute(query,values)
      connection.commit()
    print("emp saved successfully")