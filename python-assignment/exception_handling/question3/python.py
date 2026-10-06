print(" DRIVING LICENSE REGISTRATION")
class InvalidAgeForDrivingLicenseException(Exception):
    pass
class InvalidMarkForDrivingLicenseException(Exception):
    pass
class Person():
    def __init__(self,name,age,mark):
        self.name=name
        self.age=age
        self.mark=mark
    def check_eligibility(self):
        if self.age<0:
            raise InvalidAgeForDrivingLicenseException
        elif self.age<18:
            raise InvalidAgeForDrivingLicenseException
        elif self.mark<=80:
            raise InvalidMarkForDrivingLicenseException
        else:
            print(" Approved")
age=int(input("enter the age here:"))
mark=int(input("enter the candidate mark here:"))
name=input("enter the name here:")
person = Person(name, age, mark)
try:
    person.check_eligibility()
except InvalidAgeForDrivingLicenseException as e:
    print("Invalid age for driving license")
except InvalidMarkForDrivingLicenseException as e:
    print("Invalid mark for driving license")

        