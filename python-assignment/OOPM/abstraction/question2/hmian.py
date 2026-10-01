from question2.hospital_managment.hospital import (
    GeneralPatient,
    EmergencyPatient,
    InsurancePatient,
    CorporatePatient
)

# Store registered patients
patients = {}


while True:

    print("""
------------------------------------------------------------
                        MAIN MENU
------------------------------------------------------------

========================================
       HOSPITAL MANAGEMENT SYSTEM
========================================

1. Register Patient
2. Generate Patient Bill
3. View Patient Bill
4. Exit
""")

    choice = int(input("Enter your choice: "))

    match choice:

        # --------------------------------
        # 1. REGISTER PATIENT
        # --------------------------------
        case 1:

            while True:

                print("""
----------------------------------------
        REGISTER PATIENT
----------------------------------------

1. General Patient
2. Emergency Patient
3. Insurance Patient
4. Corporate Patient
5. Back to Main Menu
""")

                a = int(input("Enter your choice here: "))

                match a:

                    case 1:
                        patient_id = int(input("Enter Patient ID: "))
                        patient_name = input("Enter Patient Name: ")
                        patient_age = int(input("Enter Patient Age: "))

                        patient = GeneralPatient(
                            patient_id,
                            patient_name,
                            patient_age
                        )

                        patients[patient_id] = patient

                        print("General Patient Registered Successfully!")

                    case 2:
                        patient_id = int(input("Enter Patient ID: "))
                        patient_name = input("Enter Patient Name: ")
                        patient_age = int(input("Enter Patient Age: "))

                        patient = EmergencyPatient(
                            patient_id,
                            patient_name,
                            patient_age
                        )

                        patients[patient_id] = patient

                        print("Emergency Patient Registered Successfully!")

                    case 3:
                        patient_id = int(input("Enter Patient ID: "))
                        patient_name = input("Enter Patient Name: ")
                        patient_age = int(input("Enter Patient Age: "))

                        patient = InsurancePatient(
                            patient_id,
                            patient_name,
                            patient_age
                        )

                        patients[patient_id] = patient

                        print("Insurance Patient Registered Successfully!")

                    case 4:
                        patient_id = int(input("Enter Patient ID: "))
                        patient_name = input("Enter Patient Name: ")
                        patient_age = int(input("Enter Patient Age: "))

                        patient = CorporatePatient(
                            patient_id,
                            patient_name,
                            patient_age
                        )

                        patients[patient_id] = patient

                        print("Corporate Patient Registered Successfully!")

                    case 5:
                        break

                    case _:
                        print("Invalid choice")


        # --------------------------------
        # 2. GENERATE PATIENT BILL
        # --------------------------------
        case 2:

            patient_id = int(input("Enter Patient ID: "))

            if patient_id in patients:

                patient = patients[patient_id]

                patient.calculate_bill()
                patient.calculate_discount()
                patient.calculate_final_amount()

                print("Patient Bill Generated Successfully!")

            else:
                print("Patient not found!")


        # --------------------------------
        # 3. VIEW PATIENT BILL
        # --------------------------------
        case 3:

            patient_id = int(input("Enter Patient ID: "))

            if patient_id in patients:

                patient = patients[patient_id]

                patient.generate_bill()

            else:
                print("Patient not found!")


        # --------------------------------
        # 4. EXIT
        # --------------------------------
        case 4:

            print("Thank you for using Hospital Management System!")
            break


        # --------------------------------
        # INVALID CHOICE
        # --------------------------------
        case _:

            print("Invalid choice!")