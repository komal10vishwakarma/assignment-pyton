
from abc import ABC,abstractmethod
class Patient(ABC):
    def __init__(self,Patient_ID,Patient_Name,Patient_Age):
        self.Patient_ID=Patient_ID
        self.Patient_Name=Patient_Name
        self.Patient_Age=Patient_Age
        
       
    @abstractmethod
    def calculate_bill(self):
        pass 
    @abstractmethod
    def calculate_discount(self):
        pass 
    @abstractmethod
    def calculate_final_amount(self):
        pass 
    @abstractmethod
    def generate_bill(self):
        pass 

class GeneralPatient(Patient):
    def calculate_bill(self):

        self.consultation_fee=int(input("Enter the consultation_fee"))
        self.Room_Charge=int(input("Enter the Room_Charge       :"))
        self.Medicine_Charge=int(input("Enter the Medicine_Charge   : "))
        self.Discount =int(input("Enter the Discount          :"))
        self.days = int(input("Enter Number of Days: "))
        self.Discount = int(input("Enter Discount (%): "))
        self.total_bill = (
            self.consultation_fee
            + (self.Room_Charge * self.days)
            + self.Medicine_Charge
        )

        return self.total_bill
        
    def calculate_final_amount(self):
        self.discount_amount = self.total_bill * self.Discount / 100
        return self.discount_amount

    def calculate_discount(self):
        self.final_amount = self.total_bill - self.discount_amount
        return self.final_amount    

    def generate_bill(self):
        print("========================================")
        print("              PATIENT BILL")
        print("========================================")
        print("Patient ID       :", self.Patient_ID)
        print("Patient Name     :", self.Patient_Name)
        print("Patient Age      :", self.Patient_Age)
        print("Consultation Fee :", self.consultation_fee)
        print("Room Charge      :", self.Room_Charge)
        print("Medicine Charge  :", self.Medicine_Charge)
        print("Days             :", self.days)
        print("Total Bill       :", self.total_bill)
        print("Discount         :", self.discount_amount)
        print("Final Amount     :", self.final_amount)
        print("========================================")

# =========================================
# EMERGENCY PATIENT
# =========================================

class EmergencyPatient(Patient):
    def calculate_bill(self,Patient_ID,Patient_Name,Patient_Age):
        super().__init__(Patient_ID,Patient_Name,Patient_Age)
        self.consultation_fee=int(input("Enter the consultation_fee"))
        self.Room_Charge=int(input("Enter the Room_Charge       :"))
        self.Medicine_Charge=int(input("Enter the Medicine_Charge   : "))
        self.Discount =int(input("Enter the Discount          :"))
        self.total_bill = (
        self.consultation_fee
        + (self.Room_Charge * self.days)
        + self.Medicine_Charge
    )

        return self.total_bill

    def calculate_discount(self):
        self.discount_amount = self.total_bill * self.Discount / 100
        return self.discount_amount  

    def calculate_final_amount(self):

        self.final_amount = self.total_bill - self.discount_amount
        return self.final_amount

    def generate_bill(self):
        print("========================================")
        print("             EMERGENCY PATIENT BILL")
        print("========================================")
        print("Patient ID       :", self.Patient_ID)
        print("Patient Name     :", self.Patient_Name)
        print("Patient Age      :", self.Patient_Age)
        print("Consultation Fee :", self.consultation_fee)
        print("Room Charge      :", self.Room_Charge)
        print("Medicine Charge  :", self.Medicine_Charge)
        print("Days             :", self.days)
        print("Total Bill       :", self.total_bill)
        print("Discount         :", self.discount_amount)
        print("Final Amount     :", self.final_amount)
        print("========================================")

# =========================================
# INSURANCE PATIENT
# =========================================
class InsurancePatient(Patient):
    def calculate_bill(self,Patient_ID,Patient_Name,Patient_Age):
        super().__init__(Patient_ID,Patient_Name,Patient_Age)
        self.consultation_fee=int(input("Enter the consultation_fee"))
        self.Room_Charge=int(input("Enter the Room_Charge       :"))
        self.Discount =int(input("Enter the Discount          :")) 
        self.days=int(input("enter the days here     :"))
        self.total_bill = (
            self.consultation_fee
            + (self.Room_Charge * self.days)
            + self.Medicine_Charge
        )

        return self.total_bill

    def calculate_discount(self):
        self.Insurance_Percentage = int(
            input("Enter Insurance Coverage (%): ")
        )

        self.discount_amount = (
            self.total_bill * self.Insurance_Percentage / 100
        )
        return self.discount_amount  

    def calculate_final_amount(self):
        self.final_amount = self.total_bill - self.discount_amount
        return self.final_amount

    def generate_bill(self):
        print("========================================")
        print("              PATIENT BILL")
        print("========================================")
        print("Patient ID       :", self.Patient_ID)
        print("Patient Name     :", self.Patient_Name)
        print("Patient Age      :", self.Patient_Age)
        print("Consultation Fee :", self.consultation_fee)
        print("Room Charge      :", self.Room_Charge)
        print("Medicine Charge  :", self.Medicine_Charge)
        print("Days             :", self.days)
        print("Total Bill       :", self.total_bill)
        print("Discount         :", self.discount_amount)
        print("Final Amount     :", self.final_amount)
        print("========================================")


# =========================================
# CORPORATE PATIENT
# =========================================
class CorporatePatient(Patient):
    def calculate_bill(self,Patient_ID,Patient_Name,Patient_Age):
        super().__init__(Patient_ID,Patient_Name,Patient_Age)
        self.consultation_fee=int(input("Enter the consultation_fee"))
        self.Room_Charge=int(input("Enter the Room_Charge       :"))
        self.Medicine_Charge=int(input("Enter the Medicine_Charge   : "))
        self.Discount =int(input("Enter the Discount          :"))
        self.days=int(input*"enter the days here   :")

    def calculate_discount(self):
        # Fixed corporate discount
        self.Discount = 20

        self.discount_amount = (
            self.total_bill * self.Discount / 100
        )

        return self.discount_amount 

    def calculate_final_amount(self):
        self.final_amount = self.total_bill - self.discount_amount
        return self.final_amount

    def generate_bill(self):
        print("========================================")
        print("              PATIENT BILL")
        print("========================================")
        print("Patient ID       :", self.Patient_ID)
        print("Patient Name     :", self.Patient_Name)
        print("Patient Age      :", self.Patient_Age)
        print("Consultation Fee :", self.consultation_fee)
        print("Room Charge      :", self.Room_Charge)
        print("Medicine Charge  :", self.Medicine_Charge)
        print("Days             :", self.days)
        print("Total Bill       :", self.total_bill)
        print("Discount         :", self.discount_amount)
        print("Final Amount     :", self.final_amount)
        print("========================================")

