





# a add_doctor()
# Take doctor details:
# - Doctor ID
# - Doctor Name
# - Specialization
# - Experience
# - Consultation Fees
# Store doctor information using list and dictionary.
# b) display_doctors()
# Display all doctor details.

def add_doctor():
    doctor=[]
    n=int(input("enter number of docotrs"))
    for i in range(n):
                d={}
                doctors_id=int(input("enter doctors id"))
                doctors_name=input("enter the name of doctor")
                Specialization=input("enter the Specialization of doctor")
                Experience=input("enter the Experience of doctor")
                Consultation_Fees=int(input("enter Consultation_Fees of doctors"))
                d["id"]=doctors_id
                d["name"]=doctors_name
                d["specialist_in"]=Specialization
                d["exp"]=Experience
                d["fee_of_doc"]=Consultation_Fees
                doctor.append(d)
    print(d)
    return doctor 
add_doctor()  
        























