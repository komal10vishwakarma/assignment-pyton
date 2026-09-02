'''5. Banking Security System
   A bank validates login attempt:

* If username is "admin" → Valid user
* If password length ≥ 8 → Strong password'''
username=input("username:")
password=int(input("enter the password:"))

if username.lower()== "admin":
   print("Valid user")
if password>=8:
   print("strong password")