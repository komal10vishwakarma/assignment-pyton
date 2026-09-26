

class Rent_detailt:
    def __init__(self,monthly_rent,electricity,water,Maintenance,Internet,Other_Charges,people):
        self.monthly_rent=monthly_rent
        self.electricity=electricity
        self.water=water
        self.Maintenance=Maintenance
        self.Internet=Internet
        self.Other_Charges=Other_Charges
        self.people=people
       

    def calculation(self):
        self.total_expenses=self.monthly_rent+self.electricity+self.water+self.Maintenance+self.Internet+self.Other_Charges
        print("Total Expenses:", self.total_expenses)

    def overall(self):
        total_expenses=self.total_expenses/self.people
        print("Per Person Rent:", total_expenses)

monthly_rent=int(input("Enter Monthly Rent:"))
electricity=int(input("Enter Electricity:"))
water=int(input("Enter water"))
Maintenance=int(input("Enter Maintenance:"))
Internet=int(input("Enter Internet: "))
Other_Charges=int(input("Enter Other Charges:"))
people=int(input("Enter The Number Of People"))

obj=Rent_detailt(    monthly_rent,
    electricity,
    water,
    Maintenance,
    Internet,
    Other_Charges,
    people)
obj.calculation()
obj.overall()



