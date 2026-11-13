from connectivity import get_connection
def add():
   con=get_connection()
   c=con.cursor()
   query="insert into students(student_id,student_name,age,course) values (%s,%s,%s,%s)"
   n=int(input("enter how many students you want to add:"))
   data=[]
   for i in range(n):
        print("enter details of students---")
        student_id=int(input("enter student id:"))
        student_name=input("enter the student name here:")
        age=int(input("enter the age :"))
        course=input("enter the course here:")
        data.append((student_id,student_name,age,course))
   c.executemany(query,data)
   con.commit()
   c.close()
   con.close()
   
