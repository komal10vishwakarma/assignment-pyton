'''4. E-Commerce Discount Engine


An online shopping platform provides discounts to customers based on their total purchase amount:

* Above ₹5000 → 20% discount
* ₹2000 to ₹5000 → 10% discount
* Below ₹2000 → 5% discount

Write a Python program to calculate the final amount after discount.

Input:
Enter purchase amount: 4500

Output:
Final Amount: ₹4050'''


tp=int(input("enter your annual purchased amount:"))
if tp>5000:
   final_amt=tp-tp*0.2
   print("Final Amount:",final_amt)
elif tp>=2000 and tp<5000:
   final_amt= tp - tp*0.1
   print("Final Amount:",final_amt)
elif tp==2000:
   final_amt=tp-tp*0.05
   print("Final Amount:",final_amt)
   
