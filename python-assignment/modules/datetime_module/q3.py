# 3.A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.
salary= int(input("enter the salary : "))
service= int(input("enter the year of service: "))


if service > 5:
    bonus  = (salary*0.05)
print(f"net Bonus : {bonus}")