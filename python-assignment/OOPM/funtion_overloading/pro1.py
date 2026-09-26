class Employee():
    def __init__(self,employee_id,employee_name,salary):
        self.employee_id=employee_id
        self.employee_name=employee_name
        self.salary=salary

    def calculate_bonus(self):
        print("the employee bonus is",self.salary+300000)
   
class Developer(Employee):
    def __init__(self,employee_id,employee_name,salary):
        super().__init__(employee_id,employee_name,salary)
    def calculate_bonus(self):
        print("developer gets 10% bonus")
        self.bonus=self.salary*0.10+self.salary
        print("Total salary:", self.bonus)
        


class Manager(Employee):
    def __init__(self,employee_id,employee_name,salary):
        super().__init__(self,employee_id,employee_name,salary)
    def calculate_bonus(self):
        super().__init__(self,employee_id,employee_name,salary)
        print("manager gets 20% bonus")
        self.bonus=self.salary*0.20+self.salary
        print("Total salary:", self.bonus)

print("----- Employee Details -----")
employee_id=int(input("Employee ID :"))
employee_name=input("Employee Name :")
salary=int(input("Salary:"))
print("WHO YOU ARE 1-DEVELOPER....2-MANAGER")
Employee_type=int(input("enter"))
if Employee_type==1:
    obj=Developer(employee_id,employee_name,salary)
    
else:
    obj= Manager(employee_id,employee_name,salary)
    obj.calculate_bonus(employee_id,employee_name,salary)   

obj.calculate_bonus()
