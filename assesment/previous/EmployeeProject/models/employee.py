class Employee:
    def __init__(self,employee_id,employee_name,department,salary):
         self.employee_id   =  employee_id
         self.employee_name =employee_name
         self.department =department
         self.salary=salary
    @classmethod
    def display_all_employee(cls,emp):
         for i in emp:
              print(i.employee_id,i.employee_name,i.department,i.salary)
    @classmethod
    def  search_emplooyee_by_id(cls ,emp):
         id = int(input("Enter the employe id  to search"))
         for i in emp:
                 if i.employee_id==id:
                       print(i.employee_id,i.employee_name,i.department,i.salary)
                       break
         else:
             print("employe is not found ")
    @classmethod
    def  emp_by_dep(cls ,emp):
             id = input("Enter the employe depratment to search")
             for i in emp:
                     if i.department==id:
                           print(i.employee_id,i.employee_name,i.department,i.salary)
             else:
                 print("employe is not found ")
    @classmethod 
    def  max_sal_emp(cls,emp):
          maxsal= emp[0].salary
          e=emp[0]
          for i in emp:
                if maxsal<i.salary:
                      e=i
          print(e.employee_id,e.employee_name,e.department,e.salary)
                      
    @classmethod 
    def  emp_project(cls,emp,pro):
         id = int(input("Enter the employe depratment to search"))
         for i in pro:
                 if i.employee_id==id:
                       print(i.employee_id,i.employee_name,i.department,i.salary)

    @classmethod 
    def  max_cost_pro(cls,emp):
          maxsal= emp[0].project_cost
          e=emp[0]
          for i in emp:
                if maxsal<i.project_cost:
                      e=i
          print(e.project_id,e.project_name,e.employee_id,e.project_cost)
          

                     
       