'''8. Number Property Checker
   A system evaluates number properties:

* If number % 2 == 0 → Even number
* If number % 5 == 0 → Divisible by 5'''

number=int(input("enter the number:"))
if number % 2 == 0:
   print("even number")
if number % 5 == 0:
   print("Divisible by 5")