from datetime import datetime
# Take a date from the user in the format DD-MM-YYYY and convert it into a datetime object.

date=input("enter the date(YYYY-MM-DD)")
date=datetime.strptime(date,"%Y-%m-%d")
print(date)


date1=input("enter the date(YYYY-MM-DD)")
date1=datetime.strptime(date1,"%Y-%m-%d")
date1=datetime.strptime("full date",date1,"%Y-%B-%d")
