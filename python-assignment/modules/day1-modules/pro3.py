from datetime import datetime,timedelta

date1=input("Enter first date: (DD-MM-YYYY):")
date1=datetime.strptime(date1,"%d-%m-%Y")
print(date1)
date2=input("Enter second date: (DD-MM-YYYY):")
date2=datetime.strptime(date2,"%d-%m-%Y")
print(date2)


diff=date2-date1
print("Days Difference:",diff)

hours=diff.total_seconds()
print("Hours Difference: ",hours/3600)

minutes=hours/60
print("Minutes Difference: ",minutes)








