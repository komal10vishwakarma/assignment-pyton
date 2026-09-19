from datetime import datetime



# a) book_appointment()

# Take appointment details:
# - Appointment ID
# - Patient ID
# - Doctor ID
# - Appointment Date
# - Appointment Time

# Store appointment information.
# b) show_appointments()
# Display all booked appointments.

def book_appointment():
    appointment=[]
    n=int(input("enter how many appointment you want to book"))
    for i in range(n):
        d={}
        app_id=int(input("enter the Appointment ID"))
        patient_id=int(input("enter the Patient ID"))
        doctor_id=int(input("enter the Doctor ID")) 
        appo_date=int(input("enter date(yyyy-mm-dd)"))
        time_input=int(int("enter the Appointment Time"))
  
        d["id"]=app_id
        d["patient id"]=patient_id
        d["Doctor ID"]=doctor_id
        # d["Appointment Date"]=appo_date
        # d["Appointment Time"]=appo_time

        appointment.append(d)
    print(appointment)
    return book_appointment()



book_appointment()










