# 11. Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.
# if employee is a male and age is in between 20 to 40 then he may work in anywhere
# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
# And any other input of age should print "ERROR".  



age = int(input("Enter age: "))
sex = input("Enter sex (M/F): ")
marital = input("Enter marital status (Y/N): ")

if age < 20 or age > 60:
    print("ERROR")
elif sex == "F":
    print("She will work only in urban areas")
elif sex == "M" and age >= 20 and age <= 40:
    print("He may work anywhere")
elif sex == "M" and age > 40 and age <= 60:
    print("He will work only in urban areas")
else:
    print("ERROR")
