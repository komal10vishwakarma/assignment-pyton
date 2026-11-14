from database .connection import Database
# class Employeedao:
#     def get_employee(self):
#         print("getting emlpoyee data")
#         db=Database()
#         db.connect()

class Employeedao:
    def saveemployee(self,employee):
        print("saving employee")
        print("id",employee.id)
        print("name",employee.name)
        print("salary",employee.salary)
        db=Database()
        db.connect()