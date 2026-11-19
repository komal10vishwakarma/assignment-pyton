from service.employeeservice import  employeeservice
from model.employee import Employee
print("welcome")
employee=Employee(101,'shree',4040040)
service= employeeservice()
service.addemployee(employee)