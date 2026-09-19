# 15. Write a java program to accept the cost price of a bike
#     and display the road tax to be paid according to the 
#     following criteria.
#     Cost Price(In Rs)		Tax
#      > 100000			 15%
#      >50000 and <=100000	 10%
#      <=50000			 5%			


price= int(input("enter the percenatge  : "))


if price>100000:
    tax = price*0.15 
    print(f"tax is {tax}")
elif price>50000  and price<=100000:
    tax = price*0.10
    print(f"tax is {tax}")
elif price<=50000:
    tax = price*0.05
    print(f"tax is {tax}")
