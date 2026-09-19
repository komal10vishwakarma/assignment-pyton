# 2.A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.
quantity= int(input("enter the quantity"))
one_unit = 100
total = quantity*one_unit

if total > 1000:
    total = total - (total*0.10)
print(f"total cost for {quantity} is : {total}")