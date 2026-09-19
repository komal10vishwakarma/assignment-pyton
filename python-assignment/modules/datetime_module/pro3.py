from datetime import datetime
# Take a user's date of birth and display it in the format:
# DD/MM/YYYY.

dob=input("enter your date of birth(dd-mm-yyyy)")
dob=datetime.strptime(dob,"%d-%m-%Y")
print(dob)

# Extract and print the day, month, and year from a given date.
print(dob.year)
print(dob.month)
print(dob.day)