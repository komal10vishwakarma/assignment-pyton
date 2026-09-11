from datetime import datetime,timedelta

date=input("Enter DOB (DD-MM-YYYY):")
date=datetime.strptime(date,"%d-%m-%Y")
print(date)

today=date.today()

y1=date.year
y2=today.year
age=y2-y1
print("current age is:",age,"years")

nextbirthday=date+datetime(days=365)
print(nextbirthday)


