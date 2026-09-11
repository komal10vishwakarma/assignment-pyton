from datetime import datetime,timedelta

name=input("Enter employee name:")
date=input("Enter joining date:")
date=datetime.strptime(date,"%d-%m-%Y")
print(date)

today = datetime.today()


experience1=today.year-date.year
experience2=today.month-date.month
experience3=today.day-date.day
print("Experience:",experience1,"years:",experience2,"months:",experience3,"days")



if  experience1>=5:
	print("5 Years Completed:YES")
else:
	print("5 Years Completed:NO")


