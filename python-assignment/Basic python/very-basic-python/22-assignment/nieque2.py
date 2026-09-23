'''2. An e-commerce website provides discounts based on the cart value and user type.
The system should take cart value and user type (premium or regular) as input.
 If the cart value is greater than or equal to 5000, then check the user type. If the user is premium,
 apply a 20% discount; otherwise, apply a 10% discount. If the cart value is less than 5000,
then check if it is greater than or equal to 2000. If yes, apply a 5% discount; otherwise,
no discount is applied. Display the final payable amount.

Input:
Cart Value = 6000
User Type = Premium'''

cart_value=int(input("enter the cart value:"))
user_type=(input("enter the user typr:"))

if cart_value>=5000:
   if user_type.lower()=="premium":
      discount=cart_value*(1-20/100)
      print("apply a 20% discount ")
   else :
       if user_type.lower()=="regular":
          discount=cart_value*(1-10/100)
          print("apply a 10% discount ")

else :
     if cart_value<5000:
            if cart_value>=2000:
               discount=cart_value*(1-5/100)
               print("yes, apply a 5% discount")
     else :
        print("no discount is applied")
  