'''1. Smart Voting & ID Verification System
   A government system verifies whether a citizen can vote and whether they have a valid ID.

* If age ≥ 18 → Eligible to vote
* If ID proof is available → Allowed inside booth'''

age=int(input("enter the age:"))
id=input("do you have ID(yes/no)")

if age >=18:
       print("eligible to vote")
       if id.lower()=="yes":
           print(" Allowed inside booth")
       else:
           print("not allowed inside")

else:
       print(" not eligible for voting")
