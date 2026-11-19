from dao.employeedao import Employeedao
# class EmployeeService:
#     def getemployee(self):
#         print("service:processing employee request")
#         dao=Employeedao()
#         dao.get_employee()

class employeeservice:
    def addemployee(self,employee):
        print("service:processing")
        dao=Employeedao()
        dao.saveemployee(employee)