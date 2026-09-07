import functools 
employees = [("Rahul",45000),("Amit",30000),("Neha",55000),("Priya",40000)]
result=sorted(employees,key=lambda x:x[1])
print(result)