class Employee:
    def __init__(self,name,employee_id,salary):
        self.name=name
        self.employee_id=employee_id
        self.salary = salary
        print("RIGHT NOW YOU ARE IN THE PARENT CLASS")

    @property
    def salary(self):
        return self. __salary

    @salary.setter
    def salary(self,salary_value):
        if salary_value>0:
            self.__salary = salary_value
        else:
            print("SALARY IS VERY LESS.....GAREEB")


    @salary.deleter
    def salary(self):
        del self.__salary

    def display_details(self):
        print("Employee ID:",self.employee_id)
        print("Employee Name:",self.name)
        print("Salary:",self.salary)
        





class Developer(Employee):
    def __init__(self,name,employee_id,salary,programming_language):
        super(). __init__(name,employee_id,salary)
        self.programming_language=programming_language
        print("RIGHT NOW YOU ARE IN THE DEVELOPER CLASS")

    def display_details(self):
        super().display_details()
        print("Role:","Developer")
        print("Programming Language:",self.programming_language)

    def write_code(self):
        print(self.name, "is developing applications using", self.programming_language + ".")
    

class Manager(Employee):
    def __init__(self,name,employee_id,salary,team_size):
        super().__init__(name,employee_id,salary)
        self.team_size=team_size
        print("RIGHT NOW YOU ARE IN THE MANAGER CLASS")

    def display_details(self):
        super().display_details()
        print("Role:","Manager")
        print("teamsize",self.team_size)

    def manage_team(self):
        print(self.name,"is managing a team of",self.team_size,"members." )




employee_id = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
salary = int(input("Enter Salary: "))

print("Who are you?")
print("1. Developer")
print("2. Manager")

choice = int(input("Enter your choice: "))
if choice==1:
    programming_language = input("Enter Programming Language: ")
    obj = Developer(name, employee_id, salary, programming_language)
    print(" Employee Details")
    obj.display_details()
    obj.write_code()
elif choice ==2:
    team_size = int(input("Enter Team Size: "))
    obj = Manager(name, employee_id, salary, team_size)
    print(" Details")
    obj.display_details()
    obj.manage_team()
