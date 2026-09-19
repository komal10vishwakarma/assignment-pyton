
"""
Implement the following functions:

a) add_patient()

Take patient details from user:

- Patient ID
- Patient Name
- Age
- Gender
- Disease
- Mobile Number
"""

def add_function():
    
    patients = [ ]
    n=int(input("enter how many patients you want:"))
    for i in range(n):
        d={}
    
        id=int(input("Enter Patient ID:"))
        name=input("enter Patient Name ")
        age=int(input("Enter Age"))
        gender=input("Enter Gender")
        disease=input("Enter Disease")
        mobile=int(input("Enter Mobile Number"))
        d["ID"]=id
        d["Name"]=name
        d["Age"]=age
        d["Gender"]=gender
        d["Disease"]=disease
        d["Mobile"]=mobile
           

 
        patients.append(d)
    print(patients)
    return patients

add_function()






    
    














